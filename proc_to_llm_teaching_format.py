import json

if __name__ == '__main__':
    with open('SVAMP.json') as f, open('SVAMP.txt', 'w') as fout:
        data = json.load(f)
        for i, datum in enumerate(data):
            question = ' '.join([datum['Body'], datum['Question']])
            output = datum['Answer']
            print(f'IN: {question} OUT: {output}', file=fout, flush=True)
