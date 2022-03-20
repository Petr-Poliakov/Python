# from isOdd import isOdd

# print(isOdd(1)) #//=> false
# print(isOdd(3)) #//=> false


# from progress.bar import Bar
# import time

# with Bar('Processing', max=20) as bar:
#     for i in range(20):
#         time.sleep(0.5)
#         # Do some work
#         bar.next()



# import emoji
# print(emoji.emojize('Yana you  :thumbs_up:'))
# print(emoji.emojize("Python is fun :red_heart:"))
# print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))

# import matplotlib.pyplot as plt #### библиотека не установилась


# labels = ['G1', 'G2', 'G3', 'G4', 'G5']
# men_means = [20, 35, 30, 35, 27]
# women_means = [25, 32, 34, 20, 25]
# men_std = [2, 3, 4, 1, 2]
# women_std = [3, 5, 2, 3, 3]
# width = 0.35       # the width of the bars: can also be len(x) sequence

# fig, ax = plt.subplots()

# ax.bar(labels, men_means, width, yerr=men_std, label='Men')
# ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means,
#        label='Women')

# ax.set_ylabel('Scores')
# ax.set_title('Scores by group and gender')
# ax.legend()

# plt.show()


from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import*

updater = Updater('5212321889:AAHAOCAnBOGhqMbQWCcjk5USj58CaVIRnmU')

updater.dispatcher.add_handler(CommandHandler('hello', Hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('echo', echo_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
print('server start')
updater.start_polling()
updater.idle()