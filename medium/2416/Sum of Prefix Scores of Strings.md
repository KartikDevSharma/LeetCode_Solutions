### Appraoch 1
```Java []
class Solution {
    public int[] sumPrefixScores(String[] words) {
        int wordCount = words.length;
        Integer[] sortedIndices = new Integer[wordCount];
        for (int i = 0; i < wordCount; i++) {
            sortedIndices[i] = i;
        }
        Arrays.sort(sortedIndices, (a, b) -> words[a].compareTo(words[b]));
        
        int[] commonPrefixLengths = calculateCommonPrefixLengths(words, sortedIndices);
        int[] scores = calculateScores(words, sortedIndices, commonPrefixLengths);
        return scores;
    }

    private int[] calculateCommonPrefixLengths(String[] words, Integer[] sortedIndices) {
        int[] commonPrefixLengths = new int[words.length];
        for (int i = 1; i < words.length; i++) {
            String prevWord = words[sortedIndices[i - 1]];
            String currWord = words[sortedIndices[i]];
            int commonLength = 0;
            while (commonLength < prevWord.length() && 
                   commonLength < currWord.length() && 
                   prevWord.charAt(commonLength) == currWord.charAt(commonLength)) {
                commonLength++;
            }
            commonPrefixLengths[i] = commonLength;
        }
        return commonPrefixLengths;
    }

    private int[] calculateScores(String[] words, Integer[] sortedIndices, int[] commonPrefixLengths) {
        int[] scores = new int[words.length];
        for (int i = 0; i < sortedIndices.length; i++) {
            int wordIndex = sortedIndices[i];
            int wordLength = words[wordIndex].length();
            scores[wordIndex] += wordLength;
            int j = i + 1;
            int commonLength = wordLength;
            while (j < words.length) {
                commonLength = Math.min(commonLength, commonPrefixLengths[j]);
                if (commonLength == 0) {
                    break;
                }
                scores[wordIndex] += commonLength;
                scores[sortedIndices[j]] += commonLength;
                j++;
            }
        }
        return scores;
    }
}
//Kds Appraoch 1
```
```C++ []
class Solution {
public:
    std::vector<int> sumPrefixScores(std::vector<std::string>& words) {
        int wordCount = words.size();
        std::vector<int> sortedIndices(wordCount);
        for (int i = 0; i < wordCount; i++) {
            sortedIndices[i] = i;
        }
        std::sort(sortedIndices.begin(), sortedIndices.end(),
                  [&words](int a, int b) { return words[a] < words[b]; });
        
        std::vector<int> commonPrefixLengths = calculateCommonPrefixLengths(words, sortedIndices);
        std::vector<int> scores = calculateScores(words, sortedIndices, commonPrefixLengths);
        return scores;
    }

private:
    std::vector<int> calculateCommonPrefixLengths(const std::vector<std::string>& words, const std::vector<int>& sortedIndices) {
        std::vector<int> commonPrefixLengths(words.size(), 0);
        for (int i = 1; i < words.size(); i++) {
            const std::string& prevWord = words[sortedIndices[i - 1]];
            const std::string& currWord = words[sortedIndices[i]];
            int commonLength = 0;
            while (commonLength < prevWord.length() && 
                   commonLength < currWord.length() && 
                   prevWord[commonLength] == currWord[commonLength]) {
                commonLength++;
            }
            commonPrefixLengths[i] = commonLength;
        }
        return commonPrefixLengths;
    }

    std::vector<int> calculateScores(const std::vector<std::string>& words, const std::vector<int>& sortedIndices, const std::vector<int>& commonPrefixLengths) {
        std::vector<int> scores(words.size(), 0);
        for (int i = 0; i < sortedIndices.size(); i++) {
            int wordIndex = sortedIndices[i];
            int wordLength = words[wordIndex].length();
            scores[wordIndex] += wordLength;
            int j = i + 1;
            int commonLength = wordLength;
            while (j < words.size()) {
                commonLength = std::min(commonLength, commonPrefixLengths[j]);
                if (commonLength == 0) {
                    break;
                }
                scores[wordIndex] += commonLength;
                scores[sortedIndices[j]] += commonLength;
                j++;
            }
        }
        return scores;
    }
};
static const int KDS = []() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return 0;
}();

//KDS Appraoch 1
```
```Python []
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        word_count = len(words)
        sorted_indices = sorted(range(word_count), key=lambda i: words[i])
        common_prefix_lengths = self._calculate_common_prefix_lengths(words, sorted_indices)
        scores = self._calculate_scores(words, sorted_indices, common_prefix_lengths)
        return scores

    def _calculate_common_prefix_lengths(self, words, sorted_indices):
        common_prefix_lengths = [0] * len(words)
        for i in range(1, len(words)):
            prev_word = words[sorted_indices[i - 1]]
            curr_word = words[sorted_indices[i]]
            common_length = 0
            while (common_length < len(prev_word) and 
                   common_length < len(curr_word) and 
                   prev_word[common_length] == curr_word[common_length]):
                common_length += 1
            common_prefix_lengths[i] = common_length
        return common_prefix_lengths

    def _calculate_scores(self, words, sorted_indices, common_prefix_lengths):
        scores = [0] * len(words)
        for i, word_index in enumerate(sorted_indices):
            word_length = len(words[word_index])
            scores[word_index] += word_length
            j = i + 1
            common_length = word_length
            while j < len(words):
                common_length = min(common_length, common_prefix_lengths[j])
                if common_length == 0:
                    break
                scores[word_index] += common_length
                scores[sorted_indices[j]] += common_length
                j += 1
        return scores

#KDS Appraoch 1

```
```Go []
func sumPrefixScores(words []string) []int {
    wordCount := len(words)
    sortedIndices := make([]int, wordCount)
    for i := range sortedIndices {
        sortedIndices[i] = i
    }
    sort.Slice(sortedIndices, func(i, j int) bool {
        return words[sortedIndices[i]] < words[sortedIndices[j]]
    })

    commonPrefixLengths := calculateCommonPrefixLengths(words, sortedIndices)
    scores := calculateScores(words, sortedIndices, commonPrefixLengths)
    return scores
}

func calculateCommonPrefixLengths(words []string, sortedIndices []int) []int {
    commonPrefixLengths := make([]int, len(words))
    for i := 1; i < len(words); i++ {
        prevWord := words[sortedIndices[i-1]]
        currWord := words[sortedIndices[i]]
        commonLength := 0
        for commonLength < len(prevWord) && 
            commonLength < len(currWord) && 
            prevWord[commonLength] == currWord[commonLength] {
            commonLength++
        }
        commonPrefixLengths[i] = commonLength
    }
    return commonPrefixLengths
}

func calculateScores(words []string, sortedIndices []int, commonPrefixLengths []int) []int {
    scores := make([]int, len(words))
    for i, wordIndex := range sortedIndices {
        wordLength := len(words[wordIndex])
        scores[wordIndex] += wordLength
        j := i + 1
        commonLength := wordLength
        for j < len(words) {
            if commonLength > commonPrefixLengths[j] {
                commonLength = commonPrefixLengths[j]
            }
            if commonLength == 0 {
                break
            }
            scores[wordIndex] += commonLength
            scores[sortedIndices[j]] += commonLength
            j++
        }
    }
    return scores
}
//KDS Appraoch 1
```
```Rust []
impl Solution {
    pub fn sum_prefix_scores(words: Vec<String>) -> Vec<i32> {
        let word_count = words.len();
        let mut sorted_indices: Vec<usize> = (0..word_count).collect();
        sorted_indices.sort_by(|&a, &b| words[a].cmp(&words[b]));

        let common_prefix_lengths = Self::calculate_common_prefix_lengths(&words, &sorted_indices);
        let scores = Self::calculate_scores(&words, &sorted_indices, &common_prefix_lengths);
        scores
    }

    fn calculate_common_prefix_lengths(words: &[String], sorted_indices: &[usize]) -> Vec<usize> {
        let mut common_prefix_lengths = vec![0; words.len()];
        for i in 1..words.len() {
            let prev_word = &words[sorted_indices[i - 1]];
            let curr_word = &words[sorted_indices[i]];
            let common_length = prev_word
                .chars()
                .zip(curr_word.chars())
                .take_while(|(a, b)| a == b)
                .count();
            common_prefix_lengths[i] = common_length;
        }
        common_prefix_lengths
    }

    fn calculate_scores(words: &[String], sorted_indices: &[usize], common_prefix_lengths: &[usize]) -> Vec<i32> {
        let mut scores = vec![0; words.len()];
        for (i, &word_index) in sorted_indices.iter().enumerate() {
            let word_length = words[word_index].len();
            scores[word_index] += word_length as i32;
            let mut j = i + 1;
            let mut common_length = word_length;
            while j < words.len() {
                common_length = common_length.min(common_prefix_lengths[j]);
                if common_length == 0 {
                    break;
                }
                scores[word_index] += common_length as i32;
                scores[sorted_indices[j]] += common_length as i32;
                j += 1;
            }
        }
        scores
    }
}
//KDS Appraoch 1
```
```JavaScript []
/**
 * @param {string[]} words
 * @return {number[]}
 */
var sumPrefixScores = function(words) {
    const wordCount = words.length;
    const sortedIndices = Array.from(Array(wordCount).keys())
        .sort((a, b) => words[a].localeCompare(words[b]));
    
    const commonPrefixLengths = calculateCommonPrefixLengths(words, sortedIndices);
    const scores = calculateScores(words, sortedIndices, commonPrefixLengths);
    return scores;
};

/**
 * @param {string[]} words
 * @param {number[]} sortedIndices
 * @return {number[]}
 */
function calculateCommonPrefixLengths(words, sortedIndices) {
    const commonPrefixLengths = new Array(words.length).fill(0);
    for (let i = 1; i < words.length; i++) {
        const prevWord = words[sortedIndices[i - 1]];
        const currWord = words[sortedIndices[i]];
        let commonLength = 0;
        while (commonLength < prevWord.length && 
               commonLength < currWord.length && 
               prevWord[commonLength] === currWord[commonLength]) {
            commonLength++;
        }
        commonPrefixLengths[i] = commonLength;
    }
    return commonPrefixLengths;
}

/**
 * @param {string[]} words
 * @param {number[]} sortedIndices
 * @param {number[]} commonPrefixLengths
 * @return {number[]}
 */
function calculateScores(words, sortedIndices, commonPrefixLengths) {
    const scores = new Array(words.length).fill(0);
    for (let i = 0; i < sortedIndices.length; i++) {
        const wordIndex = sortedIndices[i];
        const wordLength = words[wordIndex].length;
        scores[wordIndex] += wordLength;
        let j = i + 1;
        let commonLength = wordLength;
        while (j < words.length) {
            commonLength = Math.min(commonLength, commonPrefixLengths[j]);
            if (commonLength === 0) {
                break;
            }
            scores[wordIndex] += commonLength;
            scores[sortedIndices[j]] += commonLength;
            j++;
        }
    }
    return scores;
}
//KDS Appraoch 1
```

### Appraoch 2
```Java []
class TrieNode {
    Map<Character, TrieNode> children;
    int count;

    TrieNode() {
        children = new HashMap<>();
        count = 0;
    }
}

class Solution {
    public int[] sumPrefixScores(String[] words) {
        TrieNode root = new TrieNode();
        
        for (String word : words) {
            TrieNode node = root;
            for (char c : word.toCharArray()) {
                node = node.children.computeIfAbsent(c, k -> new TrieNode());
                node.count++;
            }
        }
        
        int[] result = new int[words.length];
        for (int i = 0; i < words.length; i++) {
            result[i] = calculateScore(root, words[i]);
        }
        
        return result;
    }
    
    private int calculateScore(TrieNode root, String word) {
        TrieNode node = root;
        int score = 0;
        for (char c : word.toCharArray()) {
            node = node.children.get(c);
            score += node.count;
        }
        return score;
    }
}
//Kds Appraoch 2
```
```C++ []
class TrieNode {
public:
    std::unordered_map<char, TrieNode*> children;
    int count;
    
    TrieNode() : count(0) {}
    
    ~TrieNode() {
        for (auto& pair : children) {
            delete pair.second;
        }
    }
};

class Solution {
public:
    std::vector<int> sumPrefixScores(std::vector<std::string>& words) {
        TrieNode* root = new TrieNode();
        
        for (const auto& word : words) {
            TrieNode* node = root;
            for (char c : word) {
                if (node->children.find(c) == node->children.end()) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
                node->count++;
            }
        }
        
        std::vector<int> result;
        result.reserve(words.size());
        for (const auto& word : words) {
            result.push_back(calculateScore(root, word));
        }
        
        delete root;
        return result;
    }
    
private:
    int calculateScore(TrieNode* root, const std::string& word) {
        TrieNode* node = root;
        int score = 0;
        for (char c : word) {
            node = node->children[c];
            score += node->count;
        }
        return score;
    }
};
static const int KDS = []() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return 0;
}();

//KDS Appraoch 2
```
```Python []
class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = TrieNode()
        

        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                node.count += 1
        
      
        def calculate_score(word):
            node = root
            score = 0
            for char in word:
                node = node.children[char]
                score += node.count
            return score
        
 
        return [calculate_score(word) for word in words]

#KDS Appraoch 2

```
```Go []
type TrieNode struct {
    children map[rune]*TrieNode
    count    int
}

func newTrieNode() *TrieNode {
    return &TrieNode{
        children: make(map[rune]*TrieNode),
        count:    0,
    }
}

func sumPrefixScores(words []string) []int {
    root := newTrieNode()

    for _, word := range words {
        node := root
        for _, char := range word {
            if _, exists := node.children[char]; !exists {
                node.children[char] = newTrieNode()
            }
            node = node.children[char]
            node.count++
        }
    }

    result := make([]int, len(words))
    for i, word := range words {
        result[i] = calculateScore(root, word)
    }

    return result
}

func calculateScore(root *TrieNode, word string) int {
    node := root
    score := 0
    for _, char := range word {
        node = node.children[char]
        score += node.count
    }
    return score
}
//KDS Appraoch 2
```
```Rust []
use std::collections::HashMap;

struct TrieNode {
    children: HashMap<char, TrieNode>,
    count: i32,
}

impl TrieNode {
    fn new() -> Self {
        TrieNode {
            children: HashMap::new(),
            count: 0,
        }
    }
}

impl Solution {
    pub fn sum_prefix_scores(words: Vec<String>) -> Vec<i32> {
        let mut root = TrieNode::new();

        for word in &words {
            let mut node = &mut root;
            for c in word.chars() {
                node = node.children.entry(c).or_insert(TrieNode::new());
                node.count += 1;
            }
        }

        words.iter().map(|word| Self::calculate_score(&root, word)).collect()
    }

    fn calculate_score(root: &TrieNode, word: &str) -> i32 {
        let mut node = root;
        let mut score = 0;
        for c in word.chars() {
            node = node.children.get(&c).unwrap();
            score += node.count;
        }
        score
    }
}
//KDS Appraoch 2
```
```JavaScript []
class TrieNode {
    constructor() {
        this.children = new Map();
        this.count = 0;
    }
}

/**
 * @param {string[]} words
 * @return {number[]}
 */
var sumPrefixScores = function(words) {
    const root = new TrieNode();
    
    for (const word of words) {
        let node = root;
        for (const char of word) {
            if (!node.children.has(char)) {
                node.children.set(char, new TrieNode());
            }
            node = node.children.get(char);
            node.count++;
        }
    }
    
    const calculateScore = (word) => {
        let node = root;
        let score = 0;
        for (const char of word) {
            node = node.children.get(char);
            score += node.count;
        }
        return score;
    };
    
    return words.map(calculateScore);
};
//KDS Appraoch 2
```
