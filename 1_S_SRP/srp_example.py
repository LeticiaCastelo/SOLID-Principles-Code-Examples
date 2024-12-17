class Process:
    def handle(self, username: str, password: str) -> None:
        if self.__verify_input_data(username, password): # 1
            self.__verify_input_data(username, password)
            self.__verify_input_in_database(username)
            self.__insert_new_user(username, password)
        else:
            self.__raise_error('Dados Inválidos')

    def __verify_input_data(self, username: str, password: str) -> bool:
        return isinstance(username, str) and isinstance(password, str)
    
    def __verify_input_in_database(self, username: str) -> None:
        print('Acessando o banco de dados...') #2
        print('Verificando existência do usuário...')

    def __insert_new_user(self, username: str, password: str) -> None:
        print('Cadastro de usuários realizados com sucesso!') #3

    def __raise_error(self, message: str) -> Exception:
        raise Exception(message)