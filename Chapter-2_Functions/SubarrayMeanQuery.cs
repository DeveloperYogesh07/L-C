using System;

class SubarrayMeanCalculator
{
    static void Main(string[] args)
    {
        // Read N (number of elements) and Q (number of queries)
        var nq = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
        int n = nq[0];
        int q = nq[1];

        // Read array elements
        var arr = Array.ConvertAll(Console.ReadLine().Split(' '), long.Parse);

        // Precompute prefix sums
        long[] prefixSum = new long[n + 1];
        for (int i = 1; i <= n; i++)
        {
            prefixSum[i] = prefixSum[i - 1] + arr[i - 1];
        }

        // Process each query
        for (int query = 0; query < q; query++)
        {
            // Read the bounds L and R
            var bounds = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
            int l = bounds[0];
            int r = bounds[1];

            // Calculate sum of subarray [L, R]
            long subarraySum = prefixSum[r] - prefixSum[l - 1];

            // Calculate the floor of the mean
            int subarrayLength = r - l + 1;
            long meanFloor = subarraySum / subarrayLength;

            // Output the result
            Console.WriteLine(meanFloor);
        }
    }
}
