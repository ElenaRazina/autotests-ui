import pytest

SYSTEM_VERSION = 'v1.2.0'

#Если условие ложно, то тест запускается
@pytest.mark.skipif (SYSTEM_VERSION == 'v1.3.0', reason="Тест не может быть запущен, так как система имеет версию v1.3.0")
def test_system_version_valid():
    pass

#Если условие истинно, то тест пропускается 
@pytest.mark.skipif (SYSTEM_VERSION == 'v1.2.0', reason="Тест не может быть запущен, так как система имеет версию v1.2.0")
def test_system_version_invalid():
    pass