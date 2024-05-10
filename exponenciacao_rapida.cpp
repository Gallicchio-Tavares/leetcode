class Solution {
public:
    double myPow(double x, int n) { // O(log n)
        if (n == 0) return 1;

        bool negative = n < 0;
        long long modulo_n = llabs(n);

        double result = 1.0;
        while (modulo_n > 0) {
            if (modulo_n % 2 == 1) { // se não for divisível por 2
                result *= x;
            }
            x *= x;
            modulo_n /= 2;
        }

        return negative ? 1.0 / result : result;
    }
};
