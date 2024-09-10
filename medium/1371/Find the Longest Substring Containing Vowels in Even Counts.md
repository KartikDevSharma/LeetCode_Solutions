### Appraoch 1 o(n^2)
```Java []
class Solution {
    public int findTheLongestSubstring(String text) {
        Map<Character, Integer> vowelCount = new HashMap<>();
        for (char c : text.toCharArray()) {
            vowelCount.put(c, vowelCount.getOrDefault(c, 0) + 1);
        }
        boolean alternateDirection = true;
        
        for (int substringLength = text.length(); substringLength >= 0; substringLength--) {
            if (allVowelsEven(vowelCount)) {
                return substringLength;
            }
            
            if (alternateDirection) {
                vowelCount.put(text.charAt(substringLength - 1), vowelCount.get(text.charAt(substringLength - 1)) - 1);
                List<Integer> startIndices = new ArrayList<>();
                List<Integer> endIndices = new ArrayList<>();
                for (int i = 0; i < text.length() - substringLength + 1; i++) startIndices.add(i);
                for (int i = substringLength - 1; i < text.length(); i++) endIndices.add(i);
                
                if (allVowelsEven(vowelCount)) {
                    return substringLength - 1;
                }
                
                for (int i = 0; i < startIndices.size(); i++) {
                    int left = startIndices.get(i);
                    int right = endIndices.get(i);
                    vowelCount.put(text.charAt(left), vowelCount.get(text.charAt(left)) - 1);
                    vowelCount.put(text.charAt(right), vowelCount.get(text.charAt(right)) + 1);
                    if (allVowelsEven(vowelCount)) {
                        return substringLength - 1;
                    }
                }
            } else {
                vowelCount.put(text.charAt(text.length() - substringLength), vowelCount.get(text.charAt(text.length() - substringLength)) - 1);
                List<Integer> startIndices = new ArrayList<>();
                List<Integer> endIndices = new ArrayList<>();
                for (int i = substringLength - 1; i < text.length(); i++) startIndices.add(i);
                for (int i = 0; i < text.length() - substringLength + 1; i++) endIndices.add(i);
                Collections.reverse(startIndices);
                Collections.reverse(endIndices);
                
                if (allVowelsEven(vowelCount)) {
                    return substringLength - 1;
                }
                
                for (int i = 0; i < startIndices.size(); i++) {
                    int left = startIndices.get(i);
                    int right = endIndices.get(i);
                    vowelCount.put(text.charAt(left), vowelCount.get(text.charAt(left)) - 1);
                    vowelCount.put(text.charAt(right), vowelCount.get(text.charAt(right)) + 1);
                    if (allVowelsEven(vowelCount)) {
                        return substringLength - 1;
                    }
                }
            }
            
            alternateDirection = !alternateDirection;
        }
        
        return 0;
    }
    
    private boolean allVowelsEven(Map<Character, Integer> vowelCount) {
        String vowels = "aeiou";
        for (char vowel : vowels.toCharArray()) {
            if (vowelCount.getOrDefault(vowel, 0) % 2 != 0) {
                return false;
            }
        }
        return true;
    }
}

```
```C++ []
class Solution {
public:
    int findTheLongestSubstring(string text) {
        unordered_map<char, int> vowelCount;
        for (char c : text) {
            vowelCount[c]++;
        }
        bool alternateDirection = true;
        
        for (int substringLength = text.length(); substringLength >= 0; substringLength--) {
            if (allVowelsEven(vowelCount)) {
                return substringLength;
            }
            
            if (alternateDirection) {
                vowelCount[text[substringLength - 1]]--;
                vector<int> startIndices, endIndices;
                for (int i = 0; i < text.length() - substringLength + 1; i++) startIndices.push_back(i);
                for (int i = substringLength - 1; i < text.length(); i++) endIndices.push_back(i);
                
                if (allVowelsEven(vowelCount)) {
                    return substringLength - 1;
                }
                
                for (int i = 0; i < startIndices.size(); i++) {
                    int left = startIndices[i];
                    int right = endIndices[i];
                    vowelCount[text[left]]--;
                    vowelCount[text[right]]++;
                    if (allVowelsEven(vowelCount)) {
                        return substringLength - 1;
                    }
                }
            } else {
                vowelCount[text[text.length() - substringLength]]--;
                vector<int> startIndices, endIndices;
                for (int i = substringLength - 1; i < text.length(); i++) startIndices.push_back(i);
                for (int i = 0; i < text.length() - substringLength + 1; i++) endIndices.push_back(i);
                reverse(startIndices.begin(), startIndices.end());
                reverse(endIndices.begin(), endIndices.end());
                
                if (allVowelsEven(vowelCount)) {
                    return substringLength - 1;
                }
                
                for (int i = 0; i < startIndices.size(); i++) {
                    int left = startIndices[i];
                    int right = endIndices[i];
                    vowelCount[text[left]]--;
                    vowelCount[text[right]]++;
                    if (allVowelsEven(vowelCount)) {
                        return substringLength - 1;
                    }
                }
            }
            
            alternateDirection = !alternateDirection;
        }
        
        return 0;
    }
    
private:
    bool allVowelsEven(const unordered_map<char, int>& vowelCount) {
        string vowels = "aeiou";
        for (char vowel : vowels) {
            if (vowelCount.find(vowel) != vowelCount.end() && vowelCount.at(vowel) % 2 != 0) {
                return false;
            }
        }
        return true;
    }
};

```
```Python []
class Solution:
    def findTheLongestSubstring(self, text: str) -> int:
        vowel_count = Counter(text)
        alternate_direction = True
        
        for substring_length in range(len(text), -1, -1):
            if all(vowel_count[vowel] % 2 == 0 for vowel in "aeiou"):
                return substring_length
            
            if alternate_direction:
                vowel_count[text[substring_length-1]] -= 1
                start_indices = range(len(text) - substring_length + 1)
                end_indices = range(substring_length - 1, len(text))
            else:
                vowel_count[text[-substring_length]] -= 1
                start_indices = reversed(range(substring_length - 1, len(text)))
                end_indices = reversed(range(len(text) - substring_length + 1))
            
            if all(vowel_count[vowel] % 2 == 0 for vowel in "aeiou"):
                return substring_length - 1
            
            for left, right in zip(start_indices, end_indices):
                vowel_count[text[left]] -= 1
                vowel_count[text[right]] += 1
                if all(vowel_count[vowel] % 2 == 0 for vowel in "aeiou"):
                    return substring_length - 1
            
            alternate_direction = not alternate_direction
        
        return 0
#kartikdevsharmaa
def kdsmain():
    input_text = sys.stdin.read().strip()
    test_cases = input_text.splitlines()
    
    test_case_count = len(test_cases)
    output_results = []

    solver = Solution()
    for i in range(test_case_count):
        input_string = json.loads(test_cases[i])
        result = solver.findTheLongestSubstring(input_string)
        output_results.append(str(result))

    with open('user.out', 'w') as output_file:
        for result in output_results:
            output_file.write(f"{result}\n")

if __name__ == "__main__":
    kdsmain()
    exit(0)


```
```Go []
func findTheLongestSubstring(text string) int {
    vowelCount := make(map[rune]int)
    for _, c := range text {
        vowelCount[c]++
    }
    alternateDirection := true
    
    for substringLength := len(text); substringLength >= 0; substringLength-- {
        if allVowelsEven(vowelCount) {
            return substringLength
        }
        
        if alternateDirection {
            vowelCount[rune(text[substringLength-1])]--
            startIndices := make([]int, 0)
            endIndices := make([]int, 0)
            for i := 0; i < len(text) - substringLength + 1; i++ {
                startIndices = append(startIndices, i)
            }
            for i := substringLength - 1; i < len(text); i++ {
                endIndices = append(endIndices, i)
            }
            
            if allVowelsEven(vowelCount) {
                return substringLength - 1
            }
            
            for i := 0; i < len(startIndices); i++ {
                left := startIndices[i]
                right := endIndices[i]
                vowelCount[rune(text[left])]--
                vowelCount[rune(text[right])]++
                if allVowelsEven(vowelCount) {
                    return substringLength - 1
                }
            }
        } else {
            vowelCount[rune(text[len(text)-substringLength])]--
            startIndices := make([]int, 0)
            endIndices := make([]int, 0)
            for i := substringLength - 1; i < len(text); i++ {
                startIndices = append(startIndices, i)
            }
            for i := 0; i < len(text) - substringLength + 1; i++ {
                endIndices = append(endIndices, i)
            }
            reverseSlice(startIndices)
            reverseSlice(endIndices)
            
            if allVowelsEven(vowelCount) {
                return substringLength - 1
            }
            
            for i := 0; i < len(startIndices); i++ {
                left := startIndices[i]
                right := endIndices[i]
                vowelCount[rune(text[left])]--
                vowelCount[rune(text[right])]++
                if allVowelsEven(vowelCount) {
                    return substringLength - 1
                }
            }
        }
        
        alternateDirection = !alternateDirection
    }
    
    return 0
}

func allVowelsEven(vowelCount map[rune]int) bool {
    vowels := "aeiou"
    for _, vowel := range vowels {
        if vowelCount[vowel]%2 != 0 {
            return false
        }
    }
    return true
}

func reverseSlice(s []int) {
    for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
        s[i], s[j] = s[j], s[i]
    }
}

```
```Rust []

use std::collections::HashMap;

impl Solution {
    pub fn find_the_longest_substring(text: String) -> i32 {
        let mut vowel_count: HashMap<char, i32> = HashMap::new();
        for c in text.chars() {
            *vowel_count.entry(c).or_insert(0) += 1;
        }
        let mut alternate_direction = true;
        
        for substring_length in (0..=text.len()).rev() {
            if Self::all_vowels_even(&vowel_count) {
                return substring_length as i32;
            }
            
            if alternate_direction {
                *vowel_count.entry(text.chars().nth(substring_length - 1).unwrap()).or_insert(0) -= 1;
                let start_indices: Vec<usize> = (0..text.len() - substring_length + 1).collect();
                let end_indices: Vec<usize> = (substring_length - 1..text.len()).collect();
                
                if Self::all_vowels_even(&vowel_count) {
                    return (substring_length - 1) as i32;
                }
                
                for (&left, &right) in start_indices.iter().zip(end_indices.iter()) {
                    *vowel_count.entry(text.chars().nth(left).unwrap()).or_insert(0) -= 1;
                    *vowel_count.entry(text.chars().nth(right).unwrap()).or_insert(0) += 1;
                    if Self::all_vowels_even(&vowel_count) {
                        return (substring_length - 1) as i32;
                    }
                }
            } else {
                *vowel_count.entry(text.chars().nth(text.len() - substring_length).unwrap()).or_insert(0) -= 1;
                let mut start_indices: Vec<usize> = (substring_length - 1..text.len()).collect();
                let mut end_indices: Vec<usize> = (0..text.len() - substring_length + 1).collect();
                start_indices.reverse();
                end_indices.reverse();
                
                if Self::all_vowels_even(&vowel_count) {
                    return (substring_length - 1) as i32;
                }
                
                for (&left, &right) in start_indices.iter().zip(end_indices.iter()) {
                    *vowel_count.entry(text.chars().nth(left).unwrap()).or_insert(0) -= 1;
                    *vowel_count.entry(text.chars().nth(right).unwrap()).or_insert(0) += 1;
                    if Self::all_vowels_even(&vowel_count) {
                        return (substring_length - 1) as i32;
                    }
                }
            }
            
            alternate_direction = !alternate_direction;
        }
        
        0
    }
    
    fn all_vowels_even(vowel_count: &HashMap<char, i32>) -> bool {
        let vowels = ['a', 'e', 'i', 'o', 'u'];
        vowels.iter().all(|&vowel| vowel_count.get(&vowel).unwrap_or(&0) % 2 == 0)
    }
}
```
```JavaScript []


```
### Appraoch 2 o(n)
```Java []
class Solution {
    private static final int[] VOWEL_MASK = new int[128];
    static {
        VOWEL_MASK['a'] = 1;
        VOWEL_MASK['e'] = 2;
        VOWEL_MASK['i'] = 4;
        VOWEL_MASK['o'] = 8;
        VOWEL_MASK['u'] = 16;
    }

    public int findTheLongestSubstring(String s) {
        int[] firstOccurrence = new int[32];
        java.util.Arrays.fill(firstOccurrence, -2);
        firstOccurrence[0] = -1;

        int mask = 0;
        int maxLength = 0;

        for (int i = 0; i < s.length(); i++) {
            mask ^= VOWEL_MASK[s.charAt(i)];

            if (firstOccurrence[mask] == -2) {
                firstOccurrence[mask] = i;
            } else {
                maxLength = Math.max(maxLength, i - firstOccurrence[mask]);
            }
            
        }

        return maxLength;
    }
}
//kartikdevsharmaa

```
```C++ []
class Solution {
private:
    static const int VOWEL_MASK[128];

public:
    int findTheLongestSubstring(string s) {
        vector<int> firstOccurrence(32, -2);
        firstOccurrence[0] = -1;
        int mask = 0;
        int maxLength = 0;
        
        for (int i = 0; i < s.length(); i++) {
            mask ^= VOWEL_MASK[s[i]];
            if (firstOccurrence[mask] == -2) {
                firstOccurrence[mask] = i;
            } else {
                maxLength = max(maxLength, i - firstOccurrence[mask]);
            }
        }
        
        return maxLength;
    }
};

const int Solution::VOWEL_MASK[128] = {
    ['a'] = 1, ['e'] = 2, ['i'] = 4, ['o'] = 8, ['u'] = 16
};
static const auto kds = []() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return 0;
}();
//kartikdevsharmaa

```
```Python []
class Solution:
    VOWEL_MASK = {
        'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16
    }

    def findTheLongestSubstring(self, s: str) -> int:
        first_occurrence = [-2] * 32
        first_occurrence[0] = -1
        mask = 0
        max_length = 0

        for i, char in enumerate(s):
            mask ^= self.VOWEL_MASK.get(char, 0)
            if first_occurrence[mask] == -2:
                first_occurrence[mask] = i
            else:
                max_length = max(max_length, i - first_occurrence[mask])

        return max_length

def main():
    input_data = sys.stdin.read().strip()
    lines = input_data.splitlines()
    
    num_test_cases = len(lines)
    results = []

    solution = Solution()
    for i in range(num_test_cases):
        s = json.loads(lines[i])
        result = solution.findTheLongestSubstring(s)
        results.append(str(result))

    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    main()
    exit(0)

#kartikdevsharmaa

```
```Go []
func findTheLongestSubstring(s string) int {
    vowelMask := [128]int{
        'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16,
    }
    
    firstOccurrence := [32]int{}
    for i := range firstOccurrence {
        firstOccurrence[i] = -2
    }
    firstOccurrence[0] = -1
    
    mask := 0
    maxLength := 0
    
    for i, c := range s {
        mask ^= vowelMask[c]
        if firstOccurrence[mask] == -2 {
            firstOccurrence[mask] = i
        } else {
            if i - firstOccurrence[mask] > maxLength {
                maxLength = i - firstOccurrence[mask]
            }
        }
    }
    
    return maxLength
}
//karikdevsharmaa

```
```Rust []
impl Solution {
    pub fn find_the_longest_substring(s: String) -> i32 {
        let vowel_mask: [i32; 128] = {
            let mut mask = [0; 128];
            mask['a' as usize] = 1;
            mask['e' as usize] = 2;
            mask['i' as usize] = 4;
            mask['o' as usize] = 8;
            mask['u' as usize] = 16;
            mask
        };

        let mut first_occurrence = [-2; 32];
        first_occurrence[0] = -1;
        let mut mask = 0;
        let mut max_length = 0;

        for (i, c) in s.chars().enumerate() {
            mask ^= vowel_mask[c as usize];
            if first_occurrence[mask as usize] == -2 {
                first_occurrence[mask as usize] = i as i32;
            } else {
                max_length = max_length.max(i as i32 - first_occurrence[mask as usize]);
            }
        }

        max_length
    }
}

//kartikdevsharmaa

```
```JavaScript []
/**
 * @param {string} s
 * @return {number}
 */
var findTheLongestSubstring = function(s) {
    const VOWEL_MASK = {
        'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16
    };
    
    const firstOccurrence = new Array(32).fill(-2);
    firstOccurrence[0] = -1;
    
    let mask = 0;
    let maxLength = 0;
    
    for (let i = 0; i < s.length; i++) {
        mask ^= (VOWEL_MASK[s[i]] || 0);
        if (firstOccurrence[mask] === -2) {
            firstOccurrence[mask] = i;
        } else {
            maxLength = Math.max(maxLength, i - firstOccurrence[mask]);
        }
    }
    
    return maxLength;
};
//kartikdevsharmaa

```
### Approach 2 optimized 
```Java []
class Solution {
    private static final int[] CHARACTER_MAP = new int[]{1,0,0,0,2,0,0,0,4,0,0,0,0,0,8,0,0,0,0,0,16,0,0,0,0,0};
    
    public int findTheLongestSubstring(String s) {
        int[] mp = new int[32];
        Arrays.fill(mp, -1);
        
        int prefixXOR = 0;
        int longestSubstring = 0;
        mp[0] = 0;
        
        for (int i = 0; i < s.length(); i++) {
            prefixXOR ^= CHARACTER_MAP[s.charAt(i) - 'a'];
            if (mp[prefixXOR] == -1) {
                mp[prefixXOR] = i + 1;
            } else {
                longestSubstring = Math.max(longestSubstring, i - mp[prefixXOR] + 1);
            }
        }
        
        return longestSubstring;
    }
}
//KDS
```
```C++ []
class Solution {
public:
    int findTheLongestSubstring(std::string_view s) {
        static const int characterMap[26] = {1,0,0,0,2,0,0,0,4,0,0,0,0,0,8,0,0,0,0,0,16,0,0,0,0,0};
        int mp[32];
        memset(mp, -1, sizeof(mp));
        
        int prefixXOR = 0;
        int longestSubstring = 0;
        mp[0] = 0;

        for (int i = 0; i < s.length(); ++i) {
            prefixXOR ^= characterMap[s[i] - 'a'];
            if (mp[prefixXOR] == -1) {
                mp[prefixXOR] = i + 1;
            } else {
                longestSubstring = std::max(longestSubstring, i - mp[prefixXOR] + 1);
            }
        }

        return longestSubstring;
    }
};

static const auto kds = []() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return 0;
}();
//kartikdevsharmaa
```
```Python []
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        CHARACTER_MAP = [1,0,0,0,2,0,0,0,4,0,0,0,0,0,8,0,0,0,0,0,16,0,0,0,0,0]
        mp = [-1] * 32
        prefix_xor = longest_substring = 0
        mp[0] = 0
        
        for i, char in enumerate(s, 1):
            prefix_xor ^= CHARACTER_MAP[ord(char) - ord('a')]
            if mp[prefix_xor] == -1:
                mp[prefix_xor] = i
            else:
                longest_substring = max(longest_substring, i - mp[prefix_xor])
        
        return longest_substring
def kdsmain():
    input_data = sys.stdin.read().strip()
    lines = input_data.splitlines()
    
    results = []
    solution = Solution()
    for line in lines:
        try:
            s = json.loads(line)
            if not isinstance(s, str):
                raise ValueError("Input is not a string")
            result = solution.findTheLongestSubstring(s)
            results.append(str(result))
        except json.JSONDecodeError:
            results.append("Invalid JSON input")
        except ValueError as e:
            results.append(f"Error: {str(e)}")

    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    kdsmain()
    sys.exit(0)
```
```Go []
func findTheLongestSubstring(s string) int {
    characterMap := [26]int{1,0,0,0,2,0,0,0,4,0,0,0,0,0,8,0,0,0,0,0,16,0,0,0,0,0}
    mp := [32]int{}
    for i := range mp {
        mp[i] = -1
    }
    
    prefixXOR := 0
    longestSubstring := 0
    mp[0] = 0
    
    for i := 0; i < len(s); i++ {
        prefixXOR ^= characterMap[s[i] - 'a']
        if mp[prefixXOR] == -1 {
            mp[prefixXOR] = i + 1
        } else {
            if i - mp[prefixXOR] + 1 > longestSubstring {
                longestSubstring = i - mp[prefixXOR] + 1
            }
        }
    }
    
    return longestSubstring
}
```
```Rust []
impl Solution {
    pub fn find_the_longest_substring(s: String) -> i32 {
        const CHARACTER_MAP: [i32; 26] = [1,0,0,0,2,0,0,0,4,0,0,0,0,0,8,0,0,0,0,0,16,0,0,0,0,0];
        let mut mp = [-1; 32];
        let mut prefix_xor = 0;
        let mut longest_substring = 0;
        mp[0] = 0;
        
        for (i, c) in s.chars().enumerate() {
            prefix_xor ^= CHARACTER_MAP[(c as u8 - b'a') as usize];
            if mp[prefix_xor as usize] == -1 {
                mp[prefix_xor as usize] = i as i32 + 1;
            } else {
                longest_substring = longest_substring.max(i as i32 - mp[prefix_xor as usize] + 1);
            }
        }
        
        longest_substring
    }
}
```
```JavaScript []
/**
 * @param {string} s
 * @return {number}
 */
var findTheLongestSubstring = function(s) {
    const CHARACTER_MAP = [1,0,0,0,2,0,0,0,4,0,0,0,0,0,8,0,0,0,0,0,16,0,0,0,0,0];
    const mp = new Int32Array(32).fill(-1);
    let prefixXOR = 0;
    let longestSubstring = 0;
    mp[0] = 0;
    
    for (let i = 0; i < s.length; i++) {
        prefixXOR ^= CHARACTER_MAP[s.charCodeAt(i) - 97]; // 97 is the ASCII code for 'a'
        if (mp[prefixXOR] === -1) {
            mp[prefixXOR] = i + 1;
        } else {
            longestSubstring = Math.max(longestSubstring, i - mp[prefixXOR] + 1);
        }
    }
    
    return longestSubstring;
};
```
