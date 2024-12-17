public class Solution {
    public int solution(int n) {
        if (n <= 1)
        {
            return n;
        }
        int answer = 1+n;
        for (int i=2;i<n;i++)
        {
            int remain = n % i;
            if (remain == 0)
            {
                answer += i;
            }
        }
        return answer;
    }
}
