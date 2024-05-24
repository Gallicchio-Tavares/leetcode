#include <climits>
class Solution {
public:
    int reverse(int x) {
        long inverso = 0; // decleare inverso
        while (x) { // enquanto x não for zero:
            inverso = inverso * 10 + x % 10; // constroi o numero invertido:
            // x % 10 pega o resto da divisão por 10, que sempre 
            // vai ser o ultimo digito do numero x.
            // inverso * 10 vai colocar o número na posicao necessária no final
            x = x / 10;          // Update the value of x
        }
        if (inverso > INT_MAX || inverso < INT_MIN)
            return 0;
        return int(inverso);
    }
};