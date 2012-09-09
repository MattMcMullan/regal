#!/usr/bin/python -B

from string import Template, upper, replace

from ApiUtil import outputCode
from ApiUtil import typeIsVoid

from ApiCodeGen import *

from RegalDispatchLog import apiDispatchFuncInitCode
from RegalDispatchEmu import dispatchSourceTemplate
from RegalContextInfo import cond

##############################################################################################

def apiGlobalDispatchTableDefineCode(apis, args):
  categoryPrev = None
  code = ''

  code += 'struct DispatchTableGlobal {\n'
  code += '\n'
  code += '  DispatchTableGlobal();\n'
  code += '  ~DispatchTableGlobal();\n'

  for api in apis:

    code += '\n'
    if api.name in cond:
      code += '#if %s\n' % cond[api.name]

    for function in api.functions:

      if function.needsContext:
        continue

      if getattr(function,'regalOnly',False)==True:
        continue

      name   = function.name
      params = paramsDefaultCode(function.parameters, True)
      rType  = typeCode(function.ret.type)
      category  = getattr(function, 'category', None)
      version   = getattr(function, 'version', None)

      if category:
        category = category.replace('_DEPRECATED', '')
      elif version:
        category = version.replace('.', '_')
        category = 'GL_VERSION_' + category

      # Close prev if block.
      if categoryPrev and not (category == categoryPrev):
        code += '\n'

      # Begin new if block.
      if category and not (category == categoryPrev):
        code += '    // %s\n\n' % category

      code += '    %s(REGAL_CALL *%s)(%s);\n' % (rType, name, params)

      categoryPrev = category

    if api.name in cond:
      code += '#endif // %s\n' % cond[api.name]
    code += '\n'


  # Close pending if block.
  if categoryPrev:
    code += '\n'

  code += '};\n'

  return code

def apiDispatchTableDefineCode(apis, args):
  categoryPrev = None
  code = ''

  code += 'struct DispatchTable {\n'

  for api in apis:

    code += '\n'
    if api.name in cond:
      code += '#if %s\n' % cond[api.name]

    for function in api.functions:

      if not function.needsContext:
        continue

      if getattr(function,'regalOnly',False)==True:
        continue

      name   = function.name
      params = paramsDefaultCode(function.parameters, True)
      rType  = typeCode(function.ret.type)
      category  = getattr(function, 'category', None)
      version   = getattr(function, 'version', None)

      if category:
        category = category.replace('_DEPRECATED', '')
      elif version:
        category = version.replace('.', '_')
        category = 'GL_VERSION_' + category

      # Close prev if block.
      if categoryPrev and not (category == categoryPrev):
        code += '\n'

      # Begin new if block.
      if category and not (category == categoryPrev):
        code += '    // %s\n\n' % category

      code += '    %s(REGAL_CALL *%s)(%s);\n' % (rType, name, params)

      categoryPrev = category

    if api.name in cond:
      code += '#endif // %s\n' % cond[api.name]
    code += '\n'


  # Close pending if block.
  if categoryPrev:
    code += '\n'

  code += '};\n'

  return code

dispatchHeaderTemplate = Template( '''${AUTOGENERATED}
${LICENSE}

#ifndef __${HEADER_NAME}_H__
#define __${HEADER_NAME}_H__

#include "RegalUtil.h"

REGAL_GLOBAL_BEGIN

#include <GL/Regal.h>

REGAL_GLOBAL_END

REGAL_NAMESPACE_BEGIN

${API_GLOBAL_DISPATCH_TABLE_DEFINE}

extern DispatchTableGlobal dispatchTableGlobal;

${API_DISPATCH_TABLE_DEFINE}

REGAL_NAMESPACE_END

#endif // __${HEADER_NAME}_H__
''')

def generateDispatchHeader(apis, args):

  globalDispatchTableDefine = apiGlobalDispatchTableDefineCode( apis, args )
  dispatchTableDefine = apiDispatchTableDefineCode(apis, args)

  # Output

  substitute = {}

  substitute['LICENSE']         = args.license
  substitute['AUTOGENERATED']   = args.generated
  substitute['COPYRIGHT']       = args.copyright

  substitute['HEADER_NAME'] = 'REGAL_DISPATCH'
  substitute['API_GLOBAL_DISPATCH_TABLE_DEFINE'] = globalDispatchTableDefine
  substitute['API_DISPATCH_TABLE_DEFINE'] = dispatchTableDefine

  outputCode( '%s/RegalDispatch.h' % args.outdir, dispatchHeaderTemplate.substitute(substitute))
