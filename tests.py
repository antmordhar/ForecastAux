import unittest
from predecir import predecir 
from crearModelo import crearModelo
from capturaDatos import captura
import service as service
from sklearn.externals import joblib

class TestServiceARIMA(unittest.TestCase):

    def test_captura(self):
        try:
            captura()
        except ExceptionType:
            self.fail("captura() raised ExceptionType unexpectedly!")

    def test_modelo(self):
        try:
            crearModelo()
        except ExceptionType:
            self.fail("crearModelo() raised ExceptionType unexpectedly!")
    
    def test_predecir(self):
        try:
            predecir(24)
        except ExceptionType:
            self.fail("predecir() raised ExceptionType unexpectedly!")

    def test_index(self):
        response,ok=service.index()
        self.assertEqual(ok, 200)
    def test_vc(self):
        response,ok=service.vc()
        self.assertEqual(ok, 200)
    def test_co(self):
        response,ok=service.co()
        self.assertEqual(ok, 200)
    def test_sd(self):
        response,ok=service.sd()
        self.assertEqual(ok, 200)
    

if __name__ == '__main__':
    unittest.main()