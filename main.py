import utils.config
import utils.mapper
import utils.continue_watching
import colorama

colorama.init()

utils.config.set_up()
utils.mapper.map()
utils.continue_watching.continue_watching()
