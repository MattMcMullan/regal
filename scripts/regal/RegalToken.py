#!/usr/bin/python -B

from string import Template, upper, replace

from ApiUtil import outputCode
from ApiUtil import toLong
from ApiUtil import hexValue

tokenSourceTemplate = Template( '''${AUTOGENERATED}
${LICENSE}

#include "pch.h" /* For MS precompiled header support */

#include "RegalUtil.h"

REGAL_GLOBAL_BEGIN

#include "RegalPrivate.h"
#include "RegalToken.h"

#include <boost/print/string_list.hpp>
#include <boost/print/print_string.hpp>

using namespace ::boost::print;

REGAL_GLOBAL_END

REGAL_NAMESPACE_BEGIN

namespace Token {

  const char * GLbooleanToString(GLboolean v)
  {
    return v==GL_FALSE ? "GL_FALSE" : "GL_TRUE";
  }

  const char * internalFormatToString(GLint v)
  {
    const char *integer[5] = { "", "1", "2", "3", "4" };
    return 1<=v && v<=4 ? integer[v] : GLenumToString(v);
  }

  std::string
  GLtextureToString(GLenum v)
  {
    if (v>=GL_TEXTURE0 && v<=GL_TEXTURE31)
      return GLenumToString(v);

    return print_string("0x",hex(v));
  }

  std::string GLclearToString(GLbitfield v)
  {
    const GLbitfield other = v & ~(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT | GL_STENCIL_BUFFER_BIT);

    string_list<std::string> tmp;
    if (v & GL_COLOR_BUFFER_BIT)   { if (tmp.size()) tmp += " | "; tmp += "GL_COLOR_BUFFER_BIT"; }
    if (v & GL_DEPTH_BUFFER_BIT)   { if (tmp.size()) tmp += " | "; tmp += "GL_DEPTH_BUFFER_BIT"; }
    if (v & GL_STENCIL_BUFFER_BIT) { if (tmp.size()) tmp += " | "; tmp += "GL_STENCIL_BUFFER_BIT"; }
    if (other || v==0)             { if (tmp.size()) tmp += " | "; tmp += size_t(other); }

    return tmp.str();
  }

  // http://www.opengl.org/sdk/docs/man3/xhtml/glMapBufferRange.xml

  std::string GLbufferAccessToString(GLbitfield v)
  {
    const GLbitfield other = v & ~(GL_MAP_READ_BIT | GL_MAP_WRITE_BIT | GL_MAP_INVALIDATE_RANGE_BIT | GL_MAP_INVALIDATE_BUFFER_BIT | GL_MAP_FLUSH_EXPLICIT_BIT | GL_MAP_UNSYNCHRONIZED_BIT);

    string_list<std::string> tmp;
    if (v & GL_MAP_READ_BIT)              { if (tmp.size()) tmp += " | "; tmp += "GL_MAP_READ_BIT"; }
    if (v & GL_MAP_WRITE_BIT)             { if (tmp.size()) tmp += " | "; tmp += "GL_MAP_WRITE_BIT"; }
    if (v & GL_MAP_INVALIDATE_RANGE_BIT)  { if (tmp.size()) tmp += " | "; tmp += "GL_MAP_INVALIDATE_RANGE_BIT"; }
    if (v & GL_MAP_INVALIDATE_BUFFER_BIT) { if (tmp.size()) tmp += " | "; tmp += "GL_MAP_INVALIDATE_BUFFER_BIT"; }
    if (v & GL_MAP_FLUSH_EXPLICIT_BIT)    { if (tmp.size()) tmp += " | "; tmp += "GL_MAP_FLUSH_EXPLICIT_BIT"; }
    if (v & GL_MAP_UNSYNCHRONIZED_BIT)    { if (tmp.size()) tmp += " | "; tmp += "GL_MAP_UNSYNCHRONIZED_BIT"; }
    if (other || v==0)                    { if (tmp.size()) tmp += " | "; tmp += size_t(other); }

    return tmp.str();
  }

  // http://www.opengl.org/sdk/docs/man2/xhtml/glPushAttrib.xml

  std::string GLpushAttribToString(GLbitfield v)
  {
    if (v == GL_ALL_ATTRIB_BITS)
      return std::string("GL_ALL_ATTRIB_BITS");

    const GLbitfield other = v & ~(GL_ACCUM_BUFFER_BIT | GL_COLOR_BUFFER_BIT | GL_CURRENT_BIT | GL_DEPTH_BUFFER_BIT | GL_ENABLE_BIT | GL_EVAL_BIT | GL_FOG_BIT | GL_HINT_BIT | GL_LIGHTING_BIT | GL_LINE_BIT | GL_LIST_BIT | GL_MULTISAMPLE_BIT | GL_PIXEL_MODE_BIT | GL_POINT_BIT | GL_POLYGON_BIT | GL_POLYGON_STIPPLE_BIT | GL_SCISSOR_BIT | GL_STENCIL_BUFFER_BIT | GL_TEXTURE_BIT | GL_TRANSFORM_BIT | GL_VIEWPORT_BIT);

    string_list<std::string> tmp;
    if (v & GL_ACCUM_BUFFER_BIT)          { if (tmp.size()) tmp += " | "; tmp += "GL_ACCUM_BUFFER_BIT"; }
    if (v & GL_COLOR_BUFFER_BIT)          { if (tmp.size()) tmp += " | "; tmp += "GL_COLOR_BUFFER_BIT"; }
    if (v & GL_CURRENT_BIT)               { if (tmp.size()) tmp += " | "; tmp += "GL_CURRENT_BIT"; }
    if (v & GL_DEPTH_BUFFER_BIT)          { if (tmp.size()) tmp += " | "; tmp += "GL_DEPTH_BUFFER_BIT"; }
    if (v & GL_ENABLE_BIT)                { if (tmp.size()) tmp += " | "; tmp += "GL_ENABLE_BIT"; }
    if (v & GL_EVAL_BIT)                  { if (tmp.size()) tmp += " | "; tmp += "GL_EVAL_BIT"; }
    if (v & GL_FOG_BIT)                   { if (tmp.size()) tmp += " | "; tmp += "GL_FOG_BIT"; }
    if (v & GL_HINT_BIT)                  { if (tmp.size()) tmp += " | "; tmp += "GL_HINT_BIT"; }
    if (v & GL_LIGHTING_BIT)              { if (tmp.size()) tmp += " | "; tmp += "GL_LIGHTING_BIT"; }
    if (v & GL_LINE_BIT)                  { if (tmp.size()) tmp += " | "; tmp += "GL_LINE_BIT"; }
    if (v & GL_LIST_BIT)                  { if (tmp.size()) tmp += " | "; tmp += "GL_LIST_BIT"; }
    if (v & GL_MULTISAMPLE_BIT)           { if (tmp.size()) tmp += " | "; tmp += "GL_MULTISAMPLE_BIT"; }
    if (v & GL_PIXEL_MODE_BIT)            { if (tmp.size()) tmp += " | "; tmp += "GL_PIXEL_MODE_BIT"; }
    if (v & GL_POINT_BIT)                 { if (tmp.size()) tmp += " | "; tmp += "GL_POINT_BIT"; }
    if (v & GL_POLYGON_BIT)               { if (tmp.size()) tmp += " | "; tmp += "GL_POLYGON_BIT"; }
    if (v & GL_POLYGON_STIPPLE_BIT)       { if (tmp.size()) tmp += " | "; tmp += "GL_POLYGON_STIPPLE_BIT"; }
    if (v & GL_SCISSOR_BIT)               { if (tmp.size()) tmp += " | "; tmp += "GL_SCISSOR_BIT"; }
    if (v & GL_STENCIL_BUFFER_BIT)        { if (tmp.size()) tmp += " | "; tmp += "GL_STENCIL_BUFFER_BIT"; }
    if (v & GL_TEXTURE_BIT)               { if (tmp.size()) tmp += " | "; tmp += "GL_TEXTURE_BIT"; }
    if (v & GL_TRANSFORM_BIT)             { if (tmp.size()) tmp += " | "; tmp += "GL_TRANSFORM_BIT"; }
    if (v & GL_VIEWPORT_BIT)              { if (tmp.size()) tmp += " | "; tmp += "GL_VIEWPORT_BIT"; }
    if (other || v==0)                    { if (tmp.size()) tmp += " | "; tmp += size_t(other); }

    return tmp.str();
  }

  std::string GLTexParameterToString(GLenum pname, const GLfloat param)
  {
    switch (pname)
    {
      case GL_DEPTH_STENCIL_TEXTURE_MODE:
      case GL_TEXTURE_COMPARE_FUNC:
      case GL_TEXTURE_COMPARE_MODE:
      case GL_TEXTURE_MIN_FILTER:
      case GL_TEXTURE_MAG_FILTER:
      case GL_TEXTURE_SWIZZLE_R:
      case GL_TEXTURE_SWIZZLE_G:
      case GL_TEXTURE_SWIZZLE_B:
      case GL_TEXTURE_SWIZZLE_A:
      case GL_TEXTURE_WRAP_S:
      case GL_TEXTURE_WRAP_T:
      case GL_TEXTURE_WRAP_R:
        return GLenumToString(static_cast<GLenum>(param));

      default:
        return print_string(param);
    }
  }

  std::string GLTexParameterToString(GLenum pname, const GLint param)
  {
    switch (pname)
    {
      case GL_DEPTH_STENCIL_TEXTURE_MODE:
      case GL_TEXTURE_COMPARE_FUNC:
      case GL_TEXTURE_COMPARE_MODE:
      case GL_TEXTURE_MIN_FILTER:
      case GL_TEXTURE_MAG_FILTER:
      case GL_TEXTURE_SWIZZLE_R:
      case GL_TEXTURE_SWIZZLE_G:
      case GL_TEXTURE_SWIZZLE_B:
      case GL_TEXTURE_SWIZZLE_A:
      case GL_TEXTURE_WRAP_S:
      case GL_TEXTURE_WRAP_T:
      case GL_TEXTURE_WRAP_R:
        return GLenumToString(static_cast<GLenum>(param));

      default:
        return print_string(param);
    }
  }

  std::string GLTexParameterToString(GLenum pname, const GLfloat *params)
  {
    switch (pname)
    {
      case GL_DEPTH_STENCIL_TEXTURE_MODE:
      case GL_TEXTURE_COMPARE_FUNC:
      case GL_TEXTURE_COMPARE_MODE:
      case GL_TEXTURE_MIN_FILTER:
      case GL_TEXTURE_MAG_FILTER:
      case GL_TEXTURE_SWIZZLE_R:
      case GL_TEXTURE_SWIZZLE_G:
      case GL_TEXTURE_SWIZZLE_B:
      case GL_TEXTURE_SWIZZLE_A:
      case GL_TEXTURE_WRAP_S:
      case GL_TEXTURE_WRAP_T:
      case GL_TEXTURE_WRAP_R:
        return GLenumToString(static_cast<GLenum>(params[0]));

      case GL_TEXTURE_SWIZZLE_RGBA:
        return print_string(
          GLenumToString(static_cast<GLenum>(params[0])), " ",
          GLenumToString(static_cast<GLenum>(params[1])), " ",
          GLenumToString(static_cast<GLenum>(params[2])), " ",
          GLenumToString(static_cast<GLenum>(params[3])));

      default:
        return print_string(params[0]);
    }
  }

  std::string GLTexParameterToString(GLenum pname, const GLint *params)
  {
    switch (pname)
    {
      case GL_DEPTH_STENCIL_TEXTURE_MODE:
      case GL_TEXTURE_COMPARE_FUNC:
      case GL_TEXTURE_COMPARE_MODE:
      case GL_TEXTURE_MIN_FILTER:
      case GL_TEXTURE_MAG_FILTER:
      case GL_TEXTURE_SWIZZLE_R:
      case GL_TEXTURE_SWIZZLE_G:
      case GL_TEXTURE_SWIZZLE_B:
      case GL_TEXTURE_SWIZZLE_A:
      case GL_TEXTURE_WRAP_S:
      case GL_TEXTURE_WRAP_T:
      case GL_TEXTURE_WRAP_R:
        return GLenumToString(static_cast<GLenum>(params[0]));

      case GL_TEXTURE_SWIZZLE_RGBA:
        return print_string(
          GLenumToString(static_cast<GLenum>(params[0])), " ",
          GLenumToString(static_cast<GLenum>(params[1])), " ",
          GLenumToString(static_cast<GLenum>(params[2])), " ",
          GLenumToString(static_cast<GLenum>(params[3])));

      default:
        return print_string(params[0]);
    }
  }

  std::string GLTexParameterToString(GLenum pname, const GLuint *params)
  {
    switch (pname)
    {
      case GL_DEPTH_STENCIL_TEXTURE_MODE:
      case GL_TEXTURE_COMPARE_FUNC:
      case GL_TEXTURE_COMPARE_MODE:
      case GL_TEXTURE_MIN_FILTER:
      case GL_TEXTURE_MAG_FILTER:
      case GL_TEXTURE_SWIZZLE_R:
      case GL_TEXTURE_SWIZZLE_G:
      case GL_TEXTURE_SWIZZLE_B:
      case GL_TEXTURE_SWIZZLE_A:
      case GL_TEXTURE_WRAP_S:
      case GL_TEXTURE_WRAP_T:
      case GL_TEXTURE_WRAP_R:
        return GLenumToString(static_cast<GLenum>(params[0]));

      case GL_TEXTURE_SWIZZLE_RGBA:
        return print_string(
          GLenumToString(static_cast<GLenum>(params[0])), " ",
          GLenumToString(static_cast<GLenum>(params[1])), " ",
          GLenumToString(static_cast<GLenum>(params[2])), " ",
          GLenumToString(static_cast<GLenum>(params[3])));

      default:
        return print_string(params[0]);
    }
  }

${CODE}

}

REGAL_NAMESPACE_END

''')

# Filter out extension duplicates

def filterTokens(tokens):

  suffixes  = ['_ARB','_KHR','_EXT','_NV','_ATI','_PGI','_OES','_IBM','_SUN','_SGI','_SGIX','_SGIS','_APPLE','_QCOM','_ANGLE']
  suffixes2 = ['_BIT','_BITS','_BIT_NV','_BITS_NV','_BIT_PGI','_BITS_PGI','_BIT_EXT','_BITS_EXT','_BIT_SGIX','_BITS_SGIX']

  def suffixCompare(i,j):

    # Prefer anything to _BIT, _BITS

    im = [ 1 for k in suffixes2 if i.endswith(k) ]
    jm = [ 1 for k in suffixes2 if j.endswith(k) ]

    if len(im)>0 and len(jm)==0:
        return 1

    if len(im)==0 and len(jm)>0:
        return -1

    # prefer the string with none of the above suffixes

    im = [ 1 for k in suffixes if i.endswith(k) ]
    jm = [ 1 for k in suffixes if j.endswith(k) ]

    if len(im)>0 and len(jm)==0:
        return 1

    if len(im)==0 and len(jm)>0:
        return -1

    # prefer the string with earliest of the above suffixes

    for k in suffixes:
      if i.endswith(k):
        if j.endswith(k):
          return 0
        else:
          return -1
      else:
        if j.endswith(k):
          return 1

    return 0

  # Sort names into preferred suffix order

  tokens = [ (j[0], sorted(j[1],cmp=suffixCompare)) for j in tokens ]

  u = tokens

  for i in suffixes:
    u = [ (j[0], [ k for k in j[1] if not k.endswith(i)  ]) for j in u ]

  # Filter out _BIT duplicates

  for i in ['_BIT','_BITS']:
    u = [ (j[0], [ k for k in j[1] if not k.endswith(i)  ]) for j in u ]

  u = [ (i[0], [ j for j in i[1] if not j.startswith('GL_KTX_') ]) for i in u  ]

  # Form tuple of value, filtered names, all names, per GLenum

  return [ (tokens[i][0], u[i][1], tokens[i][1]) for i in xrange(len(tokens)) ]

def generateTokenSource(apis, args):

  code = []

  code.append('  const char * GLenumToString( GLenum e ) {')
  code.append('    switch( e ) {')

  for i in apis:
    if i.name != 'gl':
      continue
    e = {}
    for j in i.enums:
      if j.name != 'defines':
        continue
      for k in j.enumerants:
        value = toLong(k.value)
        if value != None:
          if not value in e:
            e[value] = set()
          e[value].add(k.name)

    e = sorted([ (i,sorted(list(e[i]))) for i in e.iterkeys() ])
    e = [ i for i in e if i[0] < 0xfffffffff ]
    e = filterTokens(e)

    for i in e:
      value = i[0]
      if len(i[1]):
        name = i[1][0]
      else:
        name = i[2][0]

      if value==0:
        name = 'GL_ZERO'
      if value==1:
        name = 'GL_ONE'

      code.append('      case %s: return "%s";'%(hexValue(value,'0x%08x'),name))

  code.append('      default: break;')
  code.append('    }')
  code.append('  return "unknown_gl_enum";')
  code.append('  }')

  # GLerrorToString

  code.append('')
  code.append('  const char * GLerrorToString( GLenum e ) {')
  code.append('    switch( e ) {')
  for i in apis:
    if i.name != 'gl':
      continue
    for j in i.enums:
      if j.name != 'defines':
        continue
      for k in j.enumerants:
        if getattr(k,'gluErrorString',None):
          code.append('      case %s: return "%s";'%(k.name,k.gluErrorString))
  code.append('      default: break;')
  code.append('    }')
  code.append('  return NULL;')
  code.append('  }')

  # GLX_VERSION

  code.append('')
  code.append('#if REGAL_SYS_GLX')
  code.append('  const char * GLXenumToString(int v) {')
  code.append('    switch( v ) {')

  for i in apis:
    if i.name != 'glx':
      continue
    e = {}
    for j in i.enums:
      if j.name != 'defines':
        continue
      for k in j.enumerants:
        value = toLong(k.value)
        if value != None:
          if not value in e:
            e[value] = set()
          e[value].add(k.name)

    e = sorted([ (i,sorted(list(e[i]))) for i in e.iterkeys() ])
    e = [ i for i in e if i[0] < 0xfffffffff ]
    e = filterTokens(e)

    for i in e:
      value = i[0]
      if len(i[1]):
        name = i[1][0]
      else:
        name = i[2][0]

      code.append('      case %s: return "%s";'%(hexValue(value,'0x%08x'),name))

  code.append('      default: break;')
  code.append('    }')
  code.append('    return "unknown_glx_enum";')
  code.append('  }')
  code.append('#endif // REGAL_SYS_GLX')

  # EGL version

  code.append('')
  code.append('#if REGAL_SYS_EGL')
  code.append('  const char * EGLenumToString(int v) {')
  code.append('    switch( v ) {')

  for i in apis:
    if i.name != 'egl':
      continue
    e = {}
    for j in i.enums:
      if j.name != 'defines':
        continue
      for k in j.enumerants:
        value = toLong(k.value)
        if value != None:
          if not value in e:
            e[value] = set()
          e[value].add(k.name)

    e = sorted([ (i,sorted(list(e[i]))) for i in e.iterkeys() ])
    e = [ i for i in e if i[0] < 0xfffffffff ]
    e = filterTokens(e)

    for i in e:
      value = i[0]
      if len(i[1]):
        name = i[1][0]
      else:
        name = i[2][0]

      if value==0:
        name = 'EGL_FALSE'
      if value==1:
        name = 'EGL_TRUE'

      code.append('      case %s: return "%s";'%(hexValue(value,'0x%08x'),name))

  code.append('      default: break;')
  code.append('    }')
  code.append('    return "unknown_egl_enum";')
  code.append('  }')
  code.append('#endif // REGAL_SYS_EGL')

  substitute = {}
  substitute['LICENSE']       = args.license
  substitute['AUTOGENERATED'] = args.generated
  substitute['COPYRIGHT']     = args.copyright
  substitute['CODE']          = '\n'.join(code)
  outputCode( '%s/RegalToken.cpp' % args.srcdir, tokenSourceTemplate.substitute(substitute))

##############################################################################################

tokenHeaderTemplate = Template( '''${AUTOGENERATED}
${LICENSE}

#ifndef __${HEADER_NAME}_H__
#define __${HEADER_NAME}_H__

#include "RegalUtil.h"

REGAL_GLOBAL_BEGIN

#include <GL/Regal.h>

#include <string>

REGAL_GLOBAL_END

REGAL_NAMESPACE_BEGIN

namespace Token {

  const char * GLenumToString        (GLenum     v);
  const char * GLerrorToString       (GLenum     v); // gluErrorString
  const char * GLbooleanToString     (GLboolean  v);
  const char * internalFormatToString(GLint      v);

  std::string  GLtextureToString     (GLenum     v); // GL_TEXTUREi or 0xaaaa

  // Bitfield strings

  std::string GLclearToString       (GLbitfield v);
  std::string GLbufferAccessToString(GLbitfield v);
  std::string GLpushAttribToString  (GLbitfield v);

  std::string GLTexParameterToString(GLenum pname, const GLfloat  param );
  std::string GLTexParameterToString(GLenum pname, const GLint    param );
  std::string GLTexParameterToString(GLenum pname, const GLfloat *params);
  std::string GLTexParameterToString(GLenum pname, const GLint   *params);
  std::string GLTexParameterToString(GLenum pname, const GLuint  *params);

  #if REGAL_SYS_GLX
  const char * GLXenumToString       (int        v);
  #endif

  #if REGAL_SYS_EGL
  const char * EGLenumToString       (int        v);
  #endif

  inline const char *toString(const GLenum    v) { return GLenumToString(v);    }
  inline const char *toString(const GLboolean v) { return GLbooleanToString(v); }
}

REGAL_NAMESPACE_END

#endif
''')

def generateTokenHeader(apis, args):

  substitute = {}
  substitute['LICENSE']       = args.license
  substitute['AUTOGENERATED'] = args.generated
  substitute['COPYRIGHT']     = args.copyright
  substitute['HEADER_NAME']   = "REGAL_TOKEN"
  outputCode( '%s/RegalToken.h' % args.srcdir, tokenHeaderTemplate.substitute(substitute))
