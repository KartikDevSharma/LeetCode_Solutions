```Java []
class Solution {
    private static final long MOD = 1000000007;
    private static final long BASE = 26;

    public String shortestPalindrome(String s) {
        if (s == null || s.length() <= 1) {
            return s;
        }

        long hash = 0;
        long reverseHash = 0;
        long power = 1;
        int len = 0;

        for (int i = 0; i < s.length(); i++) {
            hash = (hash * BASE + (s.charAt(i) - 'a' + 1)) % MOD;
            reverseHash = (reverseHash + (s.charAt(i) - 'a' + 1) * power) % MOD;
            power = (power * BASE) % MOD;

            if (hash == reverseHash) {
                len = i + 1;
            }
        }

        return new StringBuilder(s.substring(len)).reverse().toString() + s;
    }
}
//KDS

```

```C++ []
class Solution {
public:
    string shortestPalindrome(string s) {
        if (s.empty() || s.length() <= 1) {
            return s;
        }

        const long long MOD = 1000000007;
        const long long BASE = 26;

        long long hash = 0;
        long long reverseHash = 0;
        long long power = 1;
        int len = 0;

        for (int i = 0; i < s.length(); i++) {
            hash = (hash * BASE + (s[i] - 'a' + 1)) % MOD;
            reverseHash = (reverseHash + (s[i] - 'a' + 1) * power) % MOD;
            power = (power * BASE) % MOD;

            if (hash == reverseHash) {
                len = i + 1;
            }
        }

        return string(s.rbegin(), s.rbegin() + s.length() - len) + s;
    }
};
//KDS

```

```Python []
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s or len(s) <= 1:
            return s

        MOD = 1000000007
        BASE = 26

        hash_val = 0
        reverse_hash = 0
        power = 1
        length = 0

        for i, char in enumerate(s):
            hash_val = (hash_val * BASE + ord(char) - ord('a') + 1) % MOD
            reverse_hash = (reverse_hash + (ord(char) - ord('a') + 1) * power) % MOD
            power = (power * BASE) % MOD

            if hash_val == reverse_hash:
                length = i + 1

        return s[length:][::-1] + s


#KDS

```

```Go []
func shortestPalindrome(s string) string {
    if len(s) <= 1 {
        return s
    }

    const MOD int64 = 1000000007
    const BASE int64 = 26

    var hash, reverseHash, power int64 = 0, 0, 1
    var length int = 0

    for i := 0; i < len(s); i++ {
        hash = (hash*BASE + int64(s[i]-'a'+1)) % MOD
        reverseHash = (reverseHash + int64(s[i]-'a'+1)*power) % MOD
        power = (power * BASE) % MOD

        if hash == reverseHash {
            length = i + 1
        }
    }

    return reverse(s[length:]) + s
}

func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}
//KDS

```

```Rust []
impl Solution {
    pub fn shortest_palindrome(s: String) -> String {
        if s.len() <= 1 {
            return s;
        }

        const MOD: i64 = 1_000_000_007;
        const BASE: i64 = 26;

        let mut hash: i64 = 0;
        let mut reverse_hash: i64 = 0;
        let mut power: i64 = 1;
        let mut length: usize = 0;

        for (i, c) in s.chars().enumerate() {
            hash = (hash * BASE + (c as i64 - 'a' as i64 + 1)) % MOD;
            reverse_hash = (reverse_hash + (c as i64 - 'a' as i64 + 1) * power) % MOD;
            power = (power * BASE) % MOD;

            if hash == reverse_hash {
                length = i + 1;
            }
        }

        let mut result = s[length..].chars().rev().collect::<String>();
        result.push_str(&s);
        result
    }
}
//KDS

```

```JavaScript []
/**
 * @param {string} s
 * @return {string}
 */
var shortestPalindrome = function(s) {
    if (s.length <= 1) {
        return s;
    }

    const MOD = 1000000007;
    const BASE = 26;

    let hash = 0;
    let reverseHash = 0;
    let power = 1;
    let length = 0;

    for (let i = 0; i < s.length; i++) {
        hash = (hash * BASE + (s.charCodeAt(i) - 'a'.charCodeAt(0) + 1)) % MOD;
        reverseHash = (reverseHash + (s.charCodeAt(i) - 'a'.charCodeAt(0) + 1) * power) % MOD;
        power = (power * BASE) % MOD;

        if (hash === reverseHash) {
            length = i + 1;
        }
    }

    return s.slice(length).split('').reverse().join('') + s;
};
//KDS

```
