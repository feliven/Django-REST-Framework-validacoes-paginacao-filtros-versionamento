from django.db import models


# Create your models here.
class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, blank=False)
    CPF = models.CharField(max_length=11)
    data_nascimento = models.DateField(verbose_name="Data de nascimento")
    numero_celular = models.CharField(max_length=14, verbose_name="Número de celular")

    def __str__(self) -> str:
        return self.nome


class Curso(models.Model):
    OPCOES_NIVEL = [
        ("B", "Básico"),
        ("I", "Intermediário"),
        ("A", "Avançado"),
    ]

    codigo = models.CharField(max_length=10, verbose_name="Código")
    descricao = models.TextField(blank=False, verbose_name="Descrição")
    nivel = models.CharField(
        max_length=1,
        blank=False,
        null=False,
        choices=OPCOES_NIVEL,
        default="B",
        verbose_name="Nível",
    )

    def __str__(self) -> str:
        return self.codigo


class Matricula(models.Model):
    OPCOES_PERIODO = [("M", "MATUTINO"), ("V", "VESPERTINO"), ("N", "NOTURNO")]

    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(
        max_length=1,
        blank=False,
        null=False,
        choices=OPCOES_PERIODO,
        default="M",
        verbose_name="Período",
    )
