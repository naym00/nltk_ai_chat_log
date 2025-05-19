import os

class Generic:
    
    @staticmethod
    def read_file(path: str):
        response = {'flag': True, 'lines': []}
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as file:
                response['lines'] = file.readlines()
        else: response['flag'] = False
        return response
    
    @staticmethod
    def generate_summary(path: str = './static/chat.txt'):
        file_response = Generic.read_file(path)
        if file_response['flag']:
            pass
        else: pass
        print('file_response ', file_response)