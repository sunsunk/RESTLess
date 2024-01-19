import json;
def main():
    str = '''
    [
      {
        "name": "Authorization",
        "value": "Bearer glpat-BxbiYFLCrkSa77TgqjAx",
        "in": "header",
        "timeout": 600
      }
    ]
    '''
    json1 = json.loads(str)
    print(json1)
if __name__ == '__main__':
    main()