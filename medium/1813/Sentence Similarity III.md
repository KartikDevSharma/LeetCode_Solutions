```Java []

class Solution {
    public boolean areSentencesSimilar(String sentence1, String sentence2) {
        String[] words1 = sentence1.split(" ");
        String[] words2 = sentence2.split(" ");
        
        int i = 0, j = 0;
        int n1 = words1.length, n2 = words2.length;
        
        // Match words from the beginning
        while (i < n1 && i < n2 && words1[i].equals(words2[i])) {
            i++;
        }
        
        // Match words from the end
        while (j < n1 - i && j < n2 - i && words1[n1 - 1 - j].equals(words2[n2 - 1 - j])) {
            j++;
        }
        
        return i + j == Math.min(n1, n2);
    }
}
//KDS
```
```C++ []
class Solution {
public:
    bool areSentencesSimilar(string sentence1, string sentence2) {
        vector<string> words1, words2;
        istringstream iss1(sentence1), iss2(sentence2);
        string word;
        
        while (iss1 >> word) words1.push_back(word);
        while (iss2 >> word) words2.push_back(word);
        
        int i = 0, j = 0;
        int n1 = words1.size(), n2 = words2.size();
        
        while (i < n1 && i < n2 && words1[i] == words2[i]) {
            i++;
        }
        
        while (j < n1 - i && j < n2 - i && words1[n1 - 1 - j] == words2[n2 - 1 - j]) {
            j++;
        }
        
        return i + j == min(n1, n2);
    }
};
//KDS

```
```Python []

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()
        
        i = j = 0
        n1, n2 = len(words1), len(words2)
        
        while i < n1 and i < n2 and words1[i] == words2[i]:
            i += 1
        
        while j < n1 - i and j < n2 - i and words1[n1 - 1 - j] == words2[n2 - 1 - j]:
            j += 1
        
        return i + j == min(n1, n2)

#KDS

```
```Go []

func areSentencesSimilar(sentence1 string, sentence2 string) bool {
    words1 := strings.Fields(sentence1)
    words2 := strings.Fields(sentence2)
    
    i, j := 0, 0
    n1, n2 := len(words1), len(words2)
    
    for i < n1 && i < n2 && words1[i] == words2[i] {
        i++
    }
    
    for j < n1-i && j < n2-i && words1[n1-1-j] == words2[n2-1-j] {
        j++
    }
    
    return i + j == min(n1, n2)
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

```
```Rust []
impl Solution {
    pub fn are_sentences_similar(sentence1: String, sentence2: String) -> bool {
        let words1: Vec<&str> = sentence1.split_whitespace().collect();
        let words2: Vec<&str> = sentence2.split_whitespace().collect();
        
        let (mut i, mut j) = (0, 0);
        let (n1, n2) = (words1.len(), words2.len());
        
        while i < n1 && i < n2 && words1[i] == words2[i] {
            i += 1;
        }
        
        while j < n1 - i && j < n2 - i && words1[n1 - 1 - j] == words2[n2 - 1 - j] {
            j += 1;
        }
        
        i + j == n1.min(n2)
    }
}


```
```JavaScript []

/**
 * @param {string} sentence1
 * @param {string} sentence2
 * @return {boolean}
 */
var areSentencesSimilar = function(sentence1, sentence2) {
    const words1 = sentence1.split(' ');
    const words2 = sentence2.split(' ');
    
    let i = 0, j = 0;
    const n1 = words1.length, n2 = words2.length;
    
    while (i < n1 && i < n2 && words1[i] === words2[i]) {
        i++;
    }
    
    while (j < n1 - i && j < n2 - i && words1[n1 - 1 - j] === words2[n2 - 1 - j]) {
        j++;
    }
    
    return i + j === Math.min(n1, n2);
};

```
