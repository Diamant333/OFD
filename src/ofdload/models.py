from django.db import models


class Company (models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название компании')
    inn = models.CharField(max_length=12, unique=True, verbose_name='ИНН организации')
    kpp = models.CharField(max_length=9, verbose_name='КПП организации')
    token_key = models.CharField(max_length=100, unique=True, verbose_name='Токен ОФД')
    renew = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Огранизация'
        verbose_name_plural = 'Организации'
        ordering = ['name']


class Shop (models.Model):
    name = models.CharField(max_length=100, verbose_name='Название магазина')
    branch_id = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='ID в системе ОФД')
    company_id = models.ForeignKey('Company', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
        ordering = ['name']


class Kkt (models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование ККТ в ОФД')
    model = models.CharField(max_length=100, verbose_name='Модель ККТ')
    status = models.CharField(max_length=100, verbose_name='Статус кассы')
    reg_number = models.CharField(max_length=20, verbose_name='Рег.номер')
    address = models.CharField(max_length=100, verbose_name='Адрес регистрации')
    date_fn = models.CharField(max_length=30, verbose_name='Дата окончания ФН')
    company_id = models.ForeignKey('Company', on_delete=models.PROTECT)
    renew = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ККТ'
        verbose_name_plural = 'ККТ'
        ordering = ['name']

class receipts (models.Model):
    bsoCode = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Код документа БСО')
    rgId = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Id чека')
    fiscalSign = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Фискальный признак документа')
    receiptDate = models.DateTimeField(verbose_name='Дата/время чека по ККТ')
    receiptCode = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Код формы ФД')
    totalSum = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма чека')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Чек'
        verbose_name_plural = 'Чеки'
        ordering = ['fiscalSign']


class receipts_office (models.Model):
    fiscalSign = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Фискальный признак документа')
    receiptDate = models.DateTimeField(verbose_name='Дата/время чека по ККТ')
    receiptCode = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Код формы ФД')
    totalSum = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма чека')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Чек офиса'
        verbose_name_plural = 'Чеки офиса'
        ordering = ['fiscalSign']