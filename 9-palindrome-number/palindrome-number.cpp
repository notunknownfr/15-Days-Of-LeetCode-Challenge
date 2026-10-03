class Solution {
public:
    bool isPalindrome(int x) {
        string reverse="";
        string str= to_string(x);

        for(int i=str.length()-1;i>=0; --i){
            reverse+=str[i];
        }
    if (reverse==str){
        return true;
    }
    return false;
        
    }
};