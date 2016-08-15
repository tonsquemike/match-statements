# match-statements

Match source code structure blocks with regular expression.
##Synposis
Pyhton code to match if, while and for statements in source code

###Input
```sh
public static FieldsConfig getFieldsConfig(){
    if(a) {
        int i = 22:
        float j=-1.0;
        }
    while(true)
    {
        String g = "";
        float  f = 0.0;
    }
}
```
###Output
```sh
[('if', '{\r\n        int i = 22:\r\n        float j=-1.0;\r\n        }'), ('while', '{\r\n        String g = "";\r\n        float  f = 0.0;\r\n    }')]
```

## Usage
```sh
python match.py -i example.java
```
