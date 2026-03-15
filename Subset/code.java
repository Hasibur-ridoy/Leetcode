public class Main {
      public static void main(String[] args) {
        // Create an object of the Solution class
        Solution sol = new Solution();

        int[] nums = {1,2,3};
        List<List<Integer>> result = sol.subsets(nums);
        result.sort((a,b) -> b.size() - a.size());
        System.out.println("All possible subsets: " + result);
    }


  public static class Solution {
          public List<List<Integer>> subsets(int [] nums) {
              List<List<Integer>> res = new ArrayList<>();
              List<Integer> subset = new ArrayList<>();
              dfs(nums, 0, subset, res);
              return res;
          }
  
          public void dfs(int[] nums, int i, List<Integer> subset, List<List<Integer>>res){
              if (i >= nums.length) {
                  res.add(new ArrayList<>(subset));
                  return;
              }
              subset.add(nums[i]);
              dfs(nums, i+1, subset, res);
              subset.remove(subset.size() - 1);
              dfs(nums, i+1, subset, res);
          }
      }
}
