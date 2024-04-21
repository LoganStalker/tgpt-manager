import customtkinter as ctk

from .utils import BackendConnector


class MyTabView(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        self.font = ctk.CTkFont(size=14)
        super().__init__(master, **kwargs)

        self.conn = BackendConnector()

        # create tabs
        self.add("Add new bot")
        self.add("Show bots")

        # add widgets on tabs

        self.show_bots()
        self.show_add_list()

    def show_add_list(self):
        def bot_create():
            self.conn.create_bot(
                dict(
                    bot_name=bot_name_entry.get(),
                    bot_token=bot_token_entry.get(),
                    bot_api_id=bot_api_id_entry.get(),
                    bot_api_hash=bot_api_hash_entry.get(),
                    openai_api_key=openai_api_key_entry.get(),
                    openai_organization=openai_organization_entry.get(),
                    openai_assistant_id=openai_assistant_id_entry.get()
                )
            )

            self.show_bots()
            self.show_add_list()

        parent = self.tab("Add new bot")
        bot_name = ctk.CTkLabel(master=parent, font=self.font, text="Bot Name")
        bot_name.grid(row=0, column=0, padx=50, pady=5)
        bot_name_entry = ctk.CTkEntry(
            master=parent, font=self.font, placeholder_text="", width=500)
        bot_name_entry.grid(row=0, column=1, padx=10, pady=5)
        bot_token = ctk.CTkLabel(master=parent, font=self.font, text="Bot Token")
        bot_token.grid(row=1, column=0, padx=20, pady=5)
        bot_token_entry = ctk.CTkEntry(
            master=parent, font=self.font, placeholder_text="", width=500)
        bot_token_entry.grid(row=1, column=1, padx=10, pady=5)
        bot_api_id = ctk.CTkLabel(master=parent, font=self.font, text="Bot API ID")
        bot_api_id.grid(row=2, column=0, padx=20, pady=5)
        bot_api_id_entry = ctk.CTkEntry(
            master=parent, font=self.font, placeholder_text="", width=500)
        bot_api_id_entry.grid(row=2, column=1, padx=10, pady=5)
        bot_api_hash = ctk.CTkLabel(master=parent, font=self.font, text="Bot API hash")
        bot_api_hash.grid(row=3, column=0, padx=20, pady=5)
        bot_api_hash_entry = ctk.CTkEntry(
            master=parent, font=self.font, placeholder_text="", width=500)
        bot_api_hash_entry.grid(row=3, column=1, padx=10, pady=5)
        openai_api_key = ctk.CTkLabel(master=parent, font=self.font, text="OpenAI API key")
        openai_api_key.grid(row=4, column=0, padx=20, pady=5)
        openai_api_key_entry = ctk.CTkEntry(
            master=parent, font=self.font, placeholder_text="", width=500)
        openai_api_key_entry.grid(row=4, column=1, padx=10, pady=5)
        openai_organization = ctk.CTkLabel(master=parent, font=self.font, text="OpenAI Organization")
        openai_organization.grid(row=5, column=0, padx=20, pady=5)
        openai_organization_entry = ctk.CTkEntry(
            master=parent, font=self.font, placeholder_text="", width=500)
        openai_organization_entry.grid(row=5, column=1, padx=10, pady=5)
        openai_assistant_id = ctk.CTkLabel(master=parent, font=self.font, text="OpenAI Assistant ID")
        openai_assistant_id.grid(row=6, column=0, padx=20, pady=5)
        openai_assistant_id_entry = ctk.CTkEntry(
            master=parent, font=self.font, placeholder_text="", width=500)
        openai_assistant_id_entry.grid(row=6, column=1, padx=10, pady=5)
        add_bot = ctk.CTkButton(master=parent, font=self.font, text="Add Bot", command=bot_create)
        add_bot.grid(row=7, column=1, padx=10, pady=50)

    def show_bots(self):
        bots = self.conn.get_bots_list()
        tabview = ctk.CTkTabview(master=self.tab("Show bots"), width=600)
        tabview.grid(row=0, column=0, padx=15, pady=10, sticky="nsew")

        for bot in bots:
            tab_name = f"{bot['id']}"
            tb = tabview.add(tab_name)

            rows = [
                ("Bot Name :  ", bot['bot_name']),
                ("Bot Token :  ", bot['bot_token']),
                ("Bot API ID :  ", bot['bot_api_id']),
                ("Bot API hash :  ", bot['bot_api_hash']),
                ("OpenAI API key :  ", bot['openai_api_key']),
                ("OpenAI Organization :  ", bot['openai_organization']),
                ("OpenAI Assistant ID :  ", bot['openai_assistant_id']),
            ]
            for i, (param, value) in enumerate(rows):
                lable_name = ctk.CTkLabel(
                    text=param, master=tb, font=self.font, height=25, text_color="green", anchor="e")
                lable_name.grid(row=i, column=0, sticky="nsew")
                lable_value = ctk.CTkLabel(
                    text=value, master=tb, font=self.font, height=25, width=400, text_color="white", anchor="w")
                lable_value.grid(row=i, column=1, sticky="nsew")

            delete = ctk.CTkButton(master=tb, fg_color="red", text="Delete", command=lambda: bot_delete())
            delete.grid(row=9, column=2, padx=3, pady=20)

            status = ctk.CTkLabel(
                master=tb, text=bot['process_id'] and "Started" or "Stopped",
                text_color=bot['process_id'] and "green" or "red",
                font=ctk.CTkFont(size=18))
            status.grid(row=9, column=1, padx=3, pady=20)

            if bot['process_id']:
                stop = ctk.CTkButton(master=tb, text="Stop", command=lambda: stop_bot())
                stop.grid(row=9, column=0, padx=3, pady=20)
            else:
                start = ctk.CTkButton(master=tb, text="Start", command=lambda: start_bot())
                start.grid(row=9, column=0, padx=3, pady=20)

        def bot_delete():
            # delete bot here
            self.show_bots()
            self.update()

        def start_bot():
            # start bot here
            pass

        def stop_bot():
            # stop bot here
            pass


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.tab_view = MyTabView(master=self, width=750, height=550)
        self.tab_view.grid(row=0, column=0, padx=25, pady=25)
        self.maxsize(800, 600)
        self.minsize(800, 600)
        self.title("Bots manager")
