# Problem: To Lower Case
# Status: Accepted
# Language: c
# Runtime: 0 ms
# Memory: 8.7 MB
# Submitted: 2026-09-21_170857 UTC
# URL: https://leetcode.com/submissions/detail/2148909106/

char* toLowerCase(char* s) {
    for( int i=0; s[i]!='\0'; ++i){
        if( s[i] >= 65 && s[i] <= 90 ){
            s[i] = s[i]+32;
        }
    }
    return s;
}