import mock
import builtins
import main

def make_multiple_inputs(inputs):
    """ provides a function to call for every input requested. """
    def next_input(_):
        """ provides the first item in the list. """
        return inputs.pop()
    return next_input

def test_q1(capfd):
    input_output = {
        '-7': 'negativo\n',
        '3': 'positivo\n',
        '0':'zero\n',       
    }
    for k, v in input_output.items():
        with mock.patch.object(builtins, 'input', lambda _: k):
            main.q1()
            out, err = capfd.readouterr()
            assert out == v

def test_q2(capfd):
    input_output = {
        '0': 'par\n',
        '3': 'ímpar\n',
        '2':'par\n',
        '4':'par\n',
        '8':'par\n',
        '12':'par\n',
        '33':'ímpar\n',
        '99': 'ímpar\n'
    }
    for k, v in input_output.items():
        with mock.patch.object(builtins, 'input', lambda _: k):
            main.q2()
            out, err = capfd.readouterr()
            assert out == v

def test_q3(capfd, monkeypatch):
    input_output = {
        '+,3,2': '5.0\n',
        '-,2,5': '3.0\n',
        '*,4,2': '8.0\n',
        '/,2,10': '5.0\n',
    }
    for k,v in input_output.items():
        monkeypatch.setitem(__builtins__, 'input', make_multiple_inputs(k.split(',')))
        main.q3()
        out, _ = capfd.readouterr()
        assert out == v

def test_q4(capfd, monkeypatch):
    input_output = {
        '5,3,2': '5.0\n',
        '1,1,1': '1.0\n',
        '0,0,1': '1.0\n',
        '2,3,4': '4.0\n',
        '3.14, 2.71, 1.618': '3.14\n'
    }
    for k,v in input_output.items():
        monkeypatch.setitem(__builtins__, 'input', make_multiple_inputs(k.split(',')))
        main.q4()
        out, _ = capfd.readouterr()
        assert out == v

def test_q5(capfd):
    input_output = {
        '0': 'Criança\n',
        '15': 'Adolescente\n',
        '30': 'Adulto\n',
        '90': 'Idoso\n'
    }
    for k, v in input_output.items():
        with mock.patch.object(builtins, 'input', lambda _: k):
            main.q5()
            out, err = capfd.readouterr()
            assert out == v

def test_q6(capfd, monkeypatch):
    input_output = {
        '3,4,5': 'Escaleno\n',
        '5,5,5': 'Equilátero\n',
        '5,5,3': 'Isósceles\n',
        '1,1,3': 'Inválido\n',
    }
    for k,v in input_output.items():
        monkeypatch.setitem(__builtins__, 'input', make_multiple_inputs(k.split(',')))
        main.q6()
        out, _ = capfd.readouterr()
        assert out == v

def test_q7(capfd):
    input_output = {
        '0': 'F\n',
        '59': 'E\n',
        '60': 'D\n',
        '90': 'A\n'
    }
    for k, v in input_output.items():
        with mock.patch.object(builtins, 'input', lambda _: k):
            main.q7()
            out, err = capfd.readouterr()
            assert out == v

def test_q8(capfd, monkeypatch):
    input_output = {
        '12345,admin': 'Acesso concedido\n',
        '123456,admin': 'Acesso negado\n',
        '12345,usuario': 'Acesso negado\n',
        '123456,usuario': 'Acesso negado\n',
    }
    for k,v in input_output.items():
        monkeypatch.setitem(__builtins__, 'input', make_multiple_inputs(k.split(',')))
        main.q8()
        out, _ = capfd.readouterr()
        assert out == v

def test_q9(capfd, monkeypatch):
    input_output = {
        '70, 1.75': 'Peso normal\n',
        '80, 1.80': 'Peso normal\n',
        '80, 1.60': 'Obeso\n',
        '90, 1.55': 'Muito obeso\n',
    }
    for k,v in input_output.items():
        monkeypatch.setitem(__builtins__, 'input', make_multiple_inputs(k.split(',')))
        main.q9()
        out, _ = capfd.readouterr()
        assert out == v

def test_q10(capfd):
    input_output = {
        '2000': 'bissexto\n',
        '2004': 'bissexto\n',
        '1999': 'não\n'
    }
    for k, v in input_output.items():
        with mock.patch.object(builtins, 'input', lambda _: k):
            main.q10()
            out, err = capfd.readouterr()
            assert out == v