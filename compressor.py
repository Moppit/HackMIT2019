with open('/tmp/out.csv', 'r') as f:
    with open('./test.csv', 'w') as out:
        for line in f.readlines():
            line = line.split(', ')
            if '/muse/elements/beta_relative' in line[1]:
                out.write(f"{line[0]},{'beta'},{line[2]}\n")
            elif '/muse/elements/alpha_relative' in line[1]:
                out.write(f"{line[0]},{'alpha'},{line[2]}\n")
            elif '/muse/elements/jaw_clench' in line[1]:
                out.write(f"{line[0]},{'jaw_clench'},{line[2]}")
