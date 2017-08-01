Aplicativo para integração com o serviço de automatização bancária do Sienge.

O aplicativo cria um zip com os arquivos de retornos do Pagamento e Cobrança Escritural e da Conciliação Bancária e os envia para serem processados pelo Sienge.

Requisitos
-------

Python 3.6
^^^^^^^^

Dependências
-------

cefpython3
^^^^^^^^
requests
^^^^^^^^
jsonpickle
^^^^^^^^

Para instalar as dependencias do aplicativo, execute o comando na pasta em que o aplicativo for descompactado::

   pip install -r requirements.txt


Para configurar o aplicativo, edite o arquivo /app/docs/configuracao.json conforme o exemplo

/app/docs/configuracao.json
^^^^^^^^
.. code-block:: json
   
   {
      "url": "http://<url-sienge>/resteasy/CPG/v1/automatizacao/bancaria/upload",
      "url_heartbeat" : "http://<url-sienge>/resteasy/CPG/v1/automatizacao/bancaria/heartbeat",
      "token": "token de validação de acesso ao sienge",
      "path": "D:/Teste - diretório raiz onde se encontram os arquivos", 
      "pagamento" : 
      {
         "paths": [
            "pagamento/itau/0001 - repositório dos arquivos de retorno do pagamento escritural da conta 0001 do itau",
            "pagamento/bradesco/0002 - repositório dos arquivos de retorno do pagamento escritural da conta 0002 do bradesco"
         ]
      },
      "cobranca" : 
      {
         "paths": [
            "cobranca/caixa/0003 - repositório dos arquivos de retorno da cobrança escritural da conta 0003 da caixa",
            "cobranca/bb/0004 - repositório dos arquivos de retorno da cobrança escritural da conta 0004 do bb"
         ]
      },
      "conciliacao" : 
      {
         "paths": [
            "conciliacao/safra/0005 - repositório dos arquivos de retorno do pagamento escritural da conta 0005 do safra",
            "conciliacao/santander/0006 - repositório dos arquivos de retorno do pagamento escritural da conta 0006 do santander"
         ]
      }
   }
	
Execução
-------------

Após a instalação do python e das dependencias, e de editar o arquivo de configuração, executar o arquivo:

app.bat
^^^^^^^^