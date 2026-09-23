class Solution {
    public boolean consecutiveSetBits(int n) {
        String bi=Integer.toBinaryString(n);
        int count = 0;
        for(int i=0;i<bi.length()-1;i++){
            if(bi.charAt(i)=='1'&&bi.charAt(i+1)=='1'){
        
        count++;
    }}
return count ==1;
}}