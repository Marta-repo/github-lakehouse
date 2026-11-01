import os
import pytest
from pyspark.sql import SparkSession


@pytest.fixture(scope="module")
def spark():
    sesion = SparkSession.builder.master("local[1]").appName("prueba").getOrCreate()
    yield sesion
    sesion.stop()


def test_pytest_funciona():
    assert 1 + 1 == 2


def test_variables_de_github():
    assert os.environ.get("GITHUB_REPOS")


def test_spark_escribe_y_lee_delta(spark, tmp_path):
    ruta = str(tmp_path / "tabla_prueba")
    df = spark.createDataFrame([(1, "a"), (2, "b")], ["id", "valor"])
    df.write.format("delta").save(ruta)
    assert spark.read.format("delta").load(ruta).count() == 2