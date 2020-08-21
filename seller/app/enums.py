from enum import IntEnum

class OrderStatus(IntEnum):
  APROVADO = 1
  EM_VALIDACAO = 2
    
  @classmethod
  def choices(cls):
    return [(key.value, key.name) for key in cls]