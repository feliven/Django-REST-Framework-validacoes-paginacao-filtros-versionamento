import random
from django.core.management.base import BaseCommand
from faker import Faker

from escola.models import Estudante, Curso


class Command(BaseCommand):
    help = "Popula o banco de dados com 40 estudantes e 20 cursos"

    def handle(self, *args, **kwargs):
        fake = Faker("pt_BR")

        # ----- Criar Cursos -----
        niveis = ["B", "I", "A"]
        cursos_criados = []

        for i in range(1, 21):
            curso = Curso.objects.create(
                codigo=f"CUR{i:03d}",
                descricao=fake.sentence(nb_words=10),
                nivel=random.choice(niveis),
            )
            cursos_criados.append(curso)
            self.stdout.write(self.style.SUCCESS(f"Curso criado: {curso.codigo}"))

        # ----- Criar Estudantes -----
        for _ in range(40):
            estudante = Estudante.objects.create(
                nome=fake.name(),
                email=fake.unique.email(),
                CPF=fake.numerify("###########"),  # 11 dígitos
                data_nascimento=fake.date_of_birth(minimum_age=15, maximum_age=40),
                numero_celular=fake.numerify("(##) #####-####"),
            )
            self.stdout.write(self.style.SUCCESS(f"Estudante criado: {estudante.nome}"))

        self.stdout.write(
            self.style.SUCCESS("40 estudantes e 20 cursos criados com sucesso!")
        )
