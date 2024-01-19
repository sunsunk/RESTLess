import json;
def main():
    str = '''
    [
      {
        "name": "Authorization",
        "value": "token  c83f0b395af780b2c28c0246e0b70159ea8e45d5",
        "in": "header",
        "timeout": 600
      }
    ]
    '''
    json1 = json.loads(str)
    print(json1)
if __name__ == '__main__':
    main()