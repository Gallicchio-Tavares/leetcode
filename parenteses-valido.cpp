class Solution {
public:
    bool isValid(string s) {
        stack<char> char_stack;

        // Se a string tiver um número ímpar de caracteres, retorna false
        if (s.size() % 2 != 0)
            return false;

        for (char c : s) {
            if (c == '(' || c == '[' || c == '{') {
                char_stack.push(c);
            } else {
                if (char_stack.empty()) {
                    return false; // Não há caractere de abertura correspondente. ex entrada: ')()'
                }
                if ((c == ')' && char_stack.top() == '(') ||
                    (c == ']' && char_stack.top() == '[') ||
                    (c == '}' && char_stack.top() == '{')) {
                    char_stack.pop();
                } else {
                    return false; // Caractere de fechamento sem correspondência. ex: (]
                }
            }
        }

        return char_stack.empty();
    }
};