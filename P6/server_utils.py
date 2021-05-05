import termcolor
from Seq1 import Seq
import pathlib
from jinja2 import Template

from seq import Seq


def print_colored(message, color):
    import termcolor
    import colorama
    colorama.init(strip="False")
    print(termcolor.colored(message, color))


def format_command(command):
    return command.replace("\n", "").replace("\r", "")


def read_template_html_file(filename):
    from pathlib import Path
    content = Template(Path(filename).read_text())
    return content


def get(n, sequences_list):
    sequence = sequences_list[int(n)]  # n -> '1' | int('1') -> 1
    context = {
        "number": n,  # 1
        "sequence": sequence,  # ATACGATAGCA
    }
    contents = read_template_html_file("./html/get.html").render(context=context)
    return contents


def info(sequence):
    seq = Seq(sequence)
    result = f"Total length: {seq.len()}<br><br>"
    for base, count in seq.count().items():
        result += f"{base}: {count} ({seq.percentage_base(base)}%)<br><br>"
    context = {
        "sequence": seq,
        "operation": "info",
        "result": result
    }
    contents = read_template_html_file("./html/operation.html").render(context=context)
    return contents


def comp(sequence):
    seq = Seq(sequence)
    context = {
        "sequence": seq,
        "operation": "comp",
        "result": seq.complement()
    }
    contents = read_template_html_file("./html/operation.html").render(context=context)
    return contents


def rev(sequence):
    seq = Seq(sequence)
    context = {
        "sequence": seq,
        "operation": "rev",
        "result": seq.reverse()
    }
    contents = read_template_html_file("./html/operation.html").render(context=context)
    return contents


def gene(name):
    path = "./sequences/" + name + ".txt"
    seq = Seq()
    seq.read_fasta(path)
    context = {
        "gene_name": name,
        "gene_contents": seq
    }
    contents = read_template_html_file("./html/gene.html").render(context=context)
    return contents
