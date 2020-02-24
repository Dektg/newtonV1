import random

otvet =  ['Приветствую вас, сэр', 'К вашим услугам, сэр', 'Да, сэр', 'Я всегда здесь','Я тут, что вы хотите', 'Я здесь, что вы хотите','Я всегда тут','Я здесь, сэр','К вашим услугам']
unique_words = list(set(otvet))
random.shuffle(unique_words) # shuffle using default Mersenne Twister generator
random.SystemRandom().shuffle(unique_words)  # OS-provided generator
print(unique_words)