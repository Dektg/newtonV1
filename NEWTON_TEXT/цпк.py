def my_app():
    print("App is running!")
    # Your app code goes here
    print("App is exiting!")
    # On exit popup a prompt where selecting 'restart' sets restart_on_exit to True
    # Replace input() with a popup as required
    if input("Type y <return> to restart the app! ").lower() == "y":
        return True

if __name__ == "__main__":
    restart_on_exit = True
    while restart_on_exit:
        restart_on_exit = my_app()