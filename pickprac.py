import pickle
import base64

g='gASV2wAAAAAAAACMC2NvbGxlY3Rpb25zlIwLT3JkZXJlZERpY3SUk5QpUpQojAt0cmFuc2l0aW9uc5QoKEsAjA5heGVscm9kLmFjdGlvbpSMBkFjdGlvbpSTlEsAhZRSlEsAaAl0lChLAGgHSwGFlFKUSwFoDHSUKEsBaAlLAWgMdJQoSwFoDEsBaAl0lHSUjA1pbml0aWFsX3N0YXRllEsAjA5pbml0aWFsX2FjdGlvbpRoCYwKbnVtX3N0YXRlc5RLAowUbXV0YXRpb25fcHJvYmFiaWxpdHmURz+5mZmZmZmadS4='

g1=base64.b64decode(g)

g2 = pickle.loads(g1)

print(g1)
