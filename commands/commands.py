import commands.roll as roll
import commands.robeandwizardhat as robeandwizardhat 
import commands.current_state as current_state

commands = { "roll" : roll.handle_command,
            "i put on my robe and wizard hat" : robeandwizardhat.handle_command,
            "state" :  current_state.handle_command }