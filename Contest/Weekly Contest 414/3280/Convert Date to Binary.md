```Java []
class Solution {
    public String convertDateToBinary(String date) {
 
        int year = (date.charAt(0) - '0') * 1000 + (date.charAt(1) - '0') * 100 + 
                   (date.charAt(2) - '0') * 10 + (date.charAt(3) - '0');
        int month = (date.charAt(5) - '0') * 10 + (date.charAt(6) - '0');
        int day = (date.charAt(8) - '0') * 10 + (date.charAt(9) - '0');


        StringBuilder sb = new StringBuilder();
        appendBinary(sb, year).append('-');
        appendBinary(sb, month).append('-');
        appendBinary(sb, day);

        return sb.toString();
    }

    private StringBuilder appendBinary(StringBuilder sb, int num) {
        if (num == 0) {
            sb.append('0');
            return sb;
        }
        
        int mask = 1 << 30; 
        boolean leadingZero = true;
        
        while (mask > 0) {
            if ((num & mask) != 0) {
                sb.append('1');
                leadingZero = false;
            } else if (!leadingZero) {
                sb.append('0');
            }
            mask >>>= 1;
        }
        
        return sb;
    }
}
//KDS
```
```C++ []
class Solution {
public:
    string convertDateToBinary(string date) {
        int year = (date[0] - '0') * 1000 + (date[1] - '0') * 100 + 
                   (date[2] - '0') * 10 + (date[3] - '0');
        int month = (date[5] - '0') * 10 + (date[6] - '0');
        int day = (date[8] - '0') * 10 + (date[9] - '0');

        string result;
        appendBinary(result, year);
        result += '-';
        appendBinary(result, month);
        result += '-';
        appendBinary(result, day);

        return result;
    }

private:
    void appendBinary(string& s, int num) {
        if (num == 0) {
            s += '0';
            return;
        }

        int mask = 1 << 30;
        bool leadingZero = true;

        while (mask > 0) {
            if ((num & mask) != 0) {
                s += '1';
                leadingZero = false;
            } else if (!leadingZero) {
                s += '0';
            }
            mask >>= 1;
        }
    }
};
```
```Python []
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:])

        def to_binary(num):
            if num == 0:
                return '0'
            binary = ''
            mask = 1 << 30
            leading_zero = True
            while mask > 0:
                if num & mask:
                    binary += '1'
                    leading_zero = False
                elif not leading_zero:
                    binary += '0'
                mask >>= 1
            return binary

        return f"{to_binary(year)}-{to_binary(month)}-{to_binary(day)}"
```
```Go []
func convertDateToBinary(date string) string {
    year := (int(date[0])-'0')*1000 + (int(date[1])-'0')*100 + 
            (int(date[2])-'0')*10 + (int(date[3])-'0')
    month := (int(date[5])-'0')*10 + (int(date[6])-'0')
    day := (int(date[8])-'0')*10 + (int(date[9])-'0')

    var result strings.Builder

    appendBinary(&result, year)
    result.WriteByte('-')
    appendBinary(&result, month)
    result.WriteByte('-')
    appendBinary(&result, day)

    return result.String()
}

func appendBinary(s *strings.Builder, num int) {
    if num == 0 {
        s.WriteByte('0')
        return
    }

    mask := 1 << 30
    leadingZero := true

    for mask > 0 {
        if (num & mask) != 0 {
            s.WriteByte('1')
            leadingZero = false
        } else if !leadingZero {
            s.WriteByte('0')
        }
        mask >>= 1
    }
}
```
```Rust []
impl Solution {
    pub fn convert_date_to_binary(date: String) -> String {
        let year = date[0..4].parse::<i32>().unwrap();
        let month = date[5..7].parse::<i32>().unwrap();
        let day = date[8..10].parse::<i32>().unwrap();

        let mut result = String::new();
        Self::append_binary(&mut result, year);
        result.push('-');
        Self::append_binary(&mut result, month);
        result.push('-');
        Self::append_binary(&mut result, day);

        result
    }

    fn append_binary(s: &mut String, mut num: i32) {
        if num == 0 {
            s.push('0');
            return;
        }

        let mut mask = 1 << 30;
        let mut leading_zero = true;

        while mask > 0 {
            if (num & mask) != 0 {
                s.push('1');
                leading_zero = false;
            } else if !leading_zero {
                s.push('0');
            }
            mask >>= 1;
        }
    }
}
//KDS
```
```JavaScript []
/**
 * @param {string} date
 * @return {string}
 */
var convertDateToBinary = function(date) {
    const year = parseInt(date.slice(0, 4));
    const month = parseInt(date.slice(5, 7));
    const day = parseInt(date.slice(8, 10));

    const toBinary = (num) => {
        if (num === 0) return '0';
        let binary = '';
        let mask = 1 << 30;
        let leadingZero = true;

        while (mask > 0) {
            if ((num & mask) !== 0) {
                binary += '1';
                leadingZero = false;
            } else if (!leadingZero) {
                binary += '0';
            }
            mask >>>= 1;
        }
        return binary;
    };

    return `${toBinary(year)}-${toBinary(month)}-${toBinary(day)}`;
};
//KDS
```
