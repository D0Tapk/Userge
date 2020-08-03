from userge import userge, Message

LOG = userge.getLogger(__name__)  # logger object

CHANNEL = userge.getCLogger(__name__)  # channel logger object

@userge.on_cmd("greet", about="command to greet people")  # adding handler and help text to .test command
async def testing(message: Message):
   LOG.info("starting test command...")  # log to console

   await message.edit("Benvenuto!✅")  # this will be automatically deleted after 5 sec

   await CHANNEL.log("testing completed!")  # log to channel
