

class Solution {
  public:
    int myAtoi(char *s) {
        if(s==nullptr||*s=='\0') {
            return 0;
        }
        int i=0;
        int sign=1;
        long ans =0;
        while(s[i]==' |') {
            i++;
        }
        if(s[i]=='-'||s[i]=='+') {
            sign=(s[i]=='-') ?-1:1;
            i++;
        }
        while(isdigit(s[i])) {
            ans=ans*10+(s[i]-'0');
            if(sign==-1&& -ans<INT_MIN) {
                return INT_MIN;
            }
            if(sign == 1&& ans >INT_MAX  ) {
                return INT_MAX;
            }
            i++;
        }
        return (int)(sign * ans);
    }
};
