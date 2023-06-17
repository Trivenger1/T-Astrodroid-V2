import random as ran
import Data.IQ_data as i

new_list = []





for prompt_char in range(len(i.prompt_list)):
    new_sub_list = []
    for prompt in i.prompt_list[prompt_char]:
        new_prompt = prompt.replace("<br> ", "<br>")
        new_prompt = new_prompt.replace("<br>", "\n\n")
        new_prompt = new_prompt.replace("</b>", "<b>")
        new_prompt = new_prompt.replace("<b>", "**")
        new_prompt = new_prompt.replace("</i>", "<i>")
        new_prompt = new_prompt.replace("<i>", "*")
        new_sub_list.append(new_prompt)
    new_list.append(new_sub_list)


def type_check(amount: int, *args):
    if len(args) != amount:
        return False
    if amount > 6 or amount < 1:
        return False
    for ar in args:
        if type(ar) != str:
            return False
    return True


def generate_prompt1(name1: str):
    retval = new_list[0][ran.randint(0, len(new_list[0]) - 1)]
    retval = retval.replace("{A}", f'{name1}')
    return f'>>> {retval}'


def generate_prompt2(name1: str, name2: str):
    retval = new_list[1][ran.randint(0, len(new_list[0]) - 1)]
    retval = retval.replace("{A}", f'{name1}')
    retval = retval.replace("{B}", f'{name2}')
    return f'>>> {retval}'


def generate_prompt3(name1: str, name2: str, name3: str):
    retval = new_list[2][ran.randint(0, len(new_list[2]) - 1)]
    retval = retval.replace("{A}", f'{name1}')
    retval = retval.replace("{B}", f'{name2}')
    retval = retval.replace("{C}", f'{name3}')
    return f'>>> {retval}'


def generate_prompt4(name1: str, name2: str, name3: str, name4: str):
    retval = new_list[3][ran.randint(0, len(new_list[3]) - 1)]
    retval = retval.replace("{A}", f'{name1}')
    retval = retval.replace("{B}", f'{name2}')
    retval = retval.replace("{C}", f'{name3}')
    retval = retval.replace("{D}", f'{name4}')
    return f'>>> {retval}'


def generate_prompt5(name1: str, name2: str, name3: str, name4: str, name5: str):
    retval = new_list[4][ran.randint(0, len(new_list[4]) - 1)]
    retval = retval.replace("{A}", f'{name1}')
    retval = retval.replace("{B}", f'{name2}')
    retval = retval.replace("{C}", f'{name3}')
    retval = retval.replace("{D}", f'{name4}')
    retval = retval.replace("{E}", f'{name5}')
    return f'>>> {retval}'


def generate_prompt6(name1: str, name2: str, name3: str, name4: str, name5: str, name6: str):
    retval = new_list[5][ran.randint(0, len(new_list[5]) - 1)]
    retval = retval.replace("{A}", f'{name1}')
    retval = retval.replace("{B}", f'{name2}')
    retval = retval.replace("{C}", f'{name3}')
    retval = retval.replace("{D}", f'{name4}')
    retval = retval.replace("{E}", f'{name5}')
    retval = retval.replace("{F}", f'{name6}')
    return f'>>> {retval}'