from juman_psc import JumanPsc
import os


class Txt2Prt():
    def __init__(self):
        if os.name == "nt":
            command = 'jumanpp_v2'
            option = '--config=C:/jumanpp/libexec/jumandic.conf'
            self.juman = JumanPsc(command=command, option=option)
        else:
            print(os.name)
            exit()

    def main(self, dir_path):
        data = self.get_data(dir_path)
        data = self.prc_data(data)
        results = self.juman_func(data)
        print(results)

    def prc_data(self, data):
        prc_data = []
        for row in data:
            row = row.replace('\n', '')
            row = row.replace(' ', '')
            data2 = row.split('。')
            for row2 in data2:
                prc_data.append(row2)
        return prc_data

    def get_data(self, dir_path):
        data = []
        file_paths = os.listdir(path=dir_path)
        for file_path in file_paths:
            path = dir_path + '/' + file_path
            f = open(path, 'r', encoding='UTF-8')
            data.append(f.read())
        f.close()
        return data

    def juman_func(self, data):
        results = []
        for row in data:
            phs = self.juman.analysis(row)
            for ph in phs:
                print(dir(ph))
                cl = [ph.midasi, ph.hinsi, ph.bunrui, ph.imis, ph.yomi]
                results.append(cl)
        return results


if __name__ == "__main__":
    dir_path = './art_txt/art_20200101'
    txt2prt = Txt2Prt()
    txt2prt.main(dir_path)
