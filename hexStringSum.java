    // https://fishc.com.cn/thread-183696-1-1.html

    // 两个16进制字符串的字符串 "123"  "123"
    // 求加和, 输出 "246"
    public static String sum(String s1, String s2){
        // 参数校验
        if(s1 == null || s1.isEmpty()){
            return s2;
        }
        if(s2 == null || s2.isEmpty()){
            return s1;
        }

        // 比长短，并且反转存储
        String shortStr, longStr;
        if(s1.length() > s2.length()){
            shortStr = s2;
            longStr = s1;
        }else{
            shortStr = s1;
            longStr = s2;
        }
        // reverse string
        shortStr = new StringBuilder(shortStr).reverse().toString().toLowerCase();
        longStr = new StringBuilder(longStr).reverse().toString().toLowerCase();

        String result = new String();

        // 以短者开始遍历，与长者相加，形成进位
        int carry = 0;
        List<Character> list = new ArrayList<>();
        for(int i=0; i<shortStr.length(); i++){
            list.clear();
            carry = add(shortStr.charAt(i), longStr.charAt(i), carry, list);
            result = list.get(0) + result;
        }
        if(shortStr.length() == longStr.length()){
            if(carry != 0){
                result = "1" + result;
            }
        }else{
            // 进位与长者剩余位数逐个相加
            for(int i=shortStr.length(); i<longStr.length(); i++){
                list.clear();
                carry = add('0', longStr.charAt(i), carry, list);
                result = list.get(0) + result;
            }
            if(carry != 0){
                result = "1" + result;
            }
        }

        return result;
    }

    // for ascii char to get hex value
    static int[] AsciiToHexDecimalValue = new int[128];
    // for hex sum to get corresponding char without carry
    static int[] HexSumToAsciiValue;
    static{
        for(int i='0'; i <= '9'; i++){
            AsciiToHexDecimalValue[i] = i - 48;
        }
        for(int i='a'; i <= 'f'; i++){
            AsciiToHexDecimalValue[i] = i - 97 + 10;
        }

        HexSumToAsciiValue = new int[]{
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f',
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'
        };
    }

    public static int add(char c1, char c2, int carry, List<Character> result){
        int r = AsciiToHexDecimalValue[c1] + AsciiToHexDecimalValue[c2] + carry;
        result.add((char)HexSumToAsciiValue[r]);
        if(r > 15){
            return 1;
        }else{
            return 0;
        }
    }
