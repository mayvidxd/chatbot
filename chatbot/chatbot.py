
class Chatbot():

    def chatx(query, chats):

        if (type(query) != str) or (type(chats) != dict):
            return "'query' must be a string and 'chats' must be a dict."
        else:
            chat_store_box = chats.keys()
            query = str(query).casefold()
            query_contain_box = query.split()
            current_holder = ''
            count = 0
            countx = 0

            for i in chat_store_box:
                s = i.casefold()
                i_holder = s.split()
                for k in query_contain_box:
                    for n in i_holder:
                        if n == k:
                            count = count+1
                            i_holder.remove(k)
                if count > countx:
                    countx = count
                    count = 0
                    current_holder = i

            response = chats.get(current_holder)

            return response


    def chatz(query, chats):

        if (type(query) != str) or (type(chats) != list):
            return "'query' must be a string and 'chats' must be a list."
        else:
            chat_store_box = chats
            query = str(query).casefold()
            query_contain_box = query.split()
            current_holder = ''
            count = 0
            countx = 0

            for i in chat_store_box:
                s = i.casefold()
                i_holder = s.split()
                for k in query_contain_box:
                    for n in i_holder:
                        if n == k:
                            count = count+1
                            i_holder.remove(k)
                if count > countx:
                    countx = count
                    count = 0
                    current_holder = i

            response = list(chats).index(current_holder) + 1
            responsex = chats[response]

            return responsex
