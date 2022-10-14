from rest_framework import serializers
from .models import cases , labs, quarantine, sqliteseq, summery, vaccine


class casesSerializer(serializers.ModelSerializer):
    class Meta:
        model = cases
        fields = ['id', 'datetime', 'reference', 'description', 'extra']


class labsSerializer(serializers.ModelSerializer):
    class Meta:
        model = labs
        fields = ['id', 'datetime', 'province', 'name', 'city', 'sector', 'reference']


class quarantineSerializer(serializers.ModelSerializer):
    class Meta:
        model = quarantine
        fields = ['id', 'datetime', 'province', 'name', 'beds', 'reference']


class sqliteseqSerializer(serializers.ModelSerializer):
    class Meta:
        model = sqliteseq
        fields = ['name', 'seq']



class summerySerializer(serializers.ModelSerializer):
    class Meta:
        model = summery
        fields = ['id', 'datetime', 'total_test', 'total_cases', 'total_recovered', 'total_deaths', 'total_critical', 'last_test', 'last_cases', 'last_recovered', 'last_deaths', 'last_critical', 'reference']



class vaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model = summery
        fields = ['id', 'datetime', 'total_partially', 'total_fully' , 'total_doses', 'last_fully', 'last_partially', 'last_doses', 'reference']
