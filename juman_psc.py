from pyknp import Juman
import re


class JumanPsc(Juman):
    invalid_chars = [r'\xla']
    end_pattern = r'[。？?！!]'

    def juman_lines(self, input_str):
        for c in JumanPsc.invalid_chars:
            input_str = input_str.replace(c, '')
            input_str = re.sub(r'(<!\s)(?!\s)', '　', input_str)
            matchObj = re.search(r'\sつ', input_str)
            if matchObj:
                s1 = input_str[:matchObj.start() + 1]
                s2 = input_str[matchObj.start() + 1:]
                return self.juman_lines(s1) + self.juman_lines(s2)
            if len(input_str.encode()) > 4096:
                matchObj = re.search(JumanPsc.end_pattern, input_str)
                if matchObj:
                    s1 = input_str[:matchObj.start() + 1]
                    s2 = input_str[matchObj.start() + 1]
                    return self.juman_lines(s1) + self.juman_lines(s2)
        return super().juman_lines(input_str)


if __name__ == "__main__":
    juman = JumanPsc(command='jumanpp_v2',
                     option='--config=C:\jumanpp\libexec\jumandic.conf')
    mrphs = juman.analysis("明日もお休みさ")
    for m in mrphs:
        print(m.midasi)
