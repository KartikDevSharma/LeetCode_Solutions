```Java []

class Solution {
    public String[] uncommonFromSentences(String s1, String s2) {
        Map<String, Integer> wordCount = new HashMap<>();
        
        countWords(s1, wordCount);
        countWords(s2, wordCount);
        
        List<String> uncommonWords = new ArrayList<>();

        for (Map.Entry<String, Integer> entry : wordCount.entrySet()) {
            if (entry.getValue() == 1) {
                uncommonWords.add(entry.getKey());
            }
        }

        return uncommonWords.toArray(new String[0]);
    }
    
    private void countWords(String s, Map<String, Integer> wordCount) {
        int start = 0;
        int end = 0;
        int len = s.length();
        
        while (end < len) {
      
            while (end < len && s.charAt(end) != ' ') {
                end++;
            }
            
    
            String word = s.substring(start, end);
            wordCount.put(word, wordCount.getOrDefault(word, 0) + 1);
            
            end++;
            start = end;
        }
    }
}
//KDS
```

```C++ []
class Solution {
public:
    vector<string> uncommonFromSentences(string s1, string s2) {
        unordered_map<string, int> wordCount;
        
        countWords(s1, wordCount);
        countWords(s2, wordCount);
        
        vector<string> uncommonWords;
        
        for (const auto& entry : wordCount) {
            if (entry.second == 1) {
                uncommonWords.push_back(entry.first);
            }
        }
        
        return uncommonWords;
    }
    
private:
    void countWords(const string& s, unordered_map<string, int>& wordCount) {
        istringstream iss(s);
        string word;
        while (iss >> word) {
            wordCount[word]++;
        }
    }
};
//KDS
```

```Python []
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        wordCount = defaultdict(int)
        
        self.countWords(s1, wordCount)
        self.countWords(s2, wordCount)
        
        return [word for word, count in wordCount.items() if count == 1]
    
    def countWords(self, s: str, wordCount: dict) -> None:
        for word in s.split():
            wordCount[word] += 1
```

```Go []
func uncommonFromSentences(s1 string, s2 string) []string {
    wordCount := make(map[string]int)
    
    countWords(s1, wordCount)
    countWords(s2, wordCount)
    
    var uncommonWords []string
    
    for word, count := range wordCount {
        if count == 1 {
            uncommonWords = append(uncommonWords, word)
        }
    }
    
    return uncommonWords
}

func countWords(s string, wordCount map[string]int) {
    words := strings.Fields(s)
    for _, word := range words {
        wordCount[word]++
    }
}
```

```Rust []
use std::collections::HashMap;

impl Solution {
    pub fn uncommon_from_sentences(s1: String, s2: String) -> Vec<String> {
        let mut word_count = HashMap::new();
        
        Self::count_words(&s1, &mut word_count);
        Self::count_words(&s2, &mut word_count);
        
        word_count.into_iter()
            .filter(|(_, count)| *count == 1)
            .map(|(word, _)| word)
            .collect()
    }
    
    fn count_words(s: &str, word_count: &mut HashMap<String, i32>) {
        for word in s.split_whitespace() {
            *word_count.entry(word.to_string()).or_insert(0) += 1;
        }
    }
}
```

```JavaScript []
/**
 * @param {string} s1
 * @param {string} s2
 * @return {string[]}
 */
var uncommonFromSentences = function(s1, s2) {
    const wordCount = new Map();
    
    countWords(s1, wordCount);
    countWords(s2, wordCount);
    
    const uncommonWords = [];
    
    for (const [word, count] of wordCount) {
        if (count === 1) {
            uncommonWords.push(word);
        }
    }
    
    return uncommonWords;
};

function countWords(s, wordCount) {
    const words = s.split(/\s+/);
    for (const word of words) {
        wordCount.set(word, (wordCount.get(word) || 0) + 1);
    }
}
```
