import json;
def main():
    str = '''
    [
      {
        "name": "Authorization",
        "value": "Bearer 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",
        "in": "header",
        "timeout": 600
      }
    ]
    '''
    json1 = json.loads(str)
    print(json1)
if __name__ == '__main__':
    main()