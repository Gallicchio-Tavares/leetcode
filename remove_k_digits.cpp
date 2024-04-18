class Solution {
public:
    string removeKdigits(string num, int k) {
              if (k == num.length()) return "0";
 
        string resp;
        stack<char> s;
 
        for (char c : num) {
            while (!s.empty() and c < s.top() and k > 0) {
                s.pop();
                k--;
            }
            s.push(c);
        }
        while (k-- and !s.empty()) {s.pop();}
        while (!s.empty()) {
            resp += s.top();
            s.pop();
        }
        reverse(resp.begin(), resp.end());
        resp.erase(0, resp.find_first_not_of('0'));
        return resp == "" ? "0" : resp;
    }
};
