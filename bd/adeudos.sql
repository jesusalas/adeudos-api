USE [adeudos]
GO
/****** Object:  Table [dbo].[abonos]    Script Date: 30/07/2017 13:48:54 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[abonos](
	[id_abono] [int] IDENTITY(1,1) NOT NULL,
	[id_cargo] [int] NOT NULL,
	[importe] [float] NOT NULL,
	[fecha_registro] [date] NOT NULL,
	[fecha_modifico] [date] NOT NULL,
	[activo] [bit] NOT NULL,
 CONSTRAINT [PK_abonos] PRIMARY KEY CLUSTERED 
(
	[id_abono] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
/****** Object:  Table [dbo].[acreedores]    Script Date: 30/07/2017 13:48:55 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[acreedores](
	[id_acreedor] [int] IDENTITY(1,1) NOT NULL,
	[nombre] [varchar](50) NOT NULL,
	[activo] [bit] NOT NULL,
 CONSTRAINT [PK_acreedores] PRIMARY KEY CLUSTERED 
(
	[id_acreedor] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[cargos]    Script Date: 30/07/2017 13:48:55 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[cargos](
	[id_cargo] [int] IDENTITY(1,1) NOT NULL,
	[importe] [float] NOT NULL,
	[descripcion] [varchar](100) NOT NULL,
	[meses] [bit] NOT NULL,
	[fecha_inicio] [nchar](10) NOT NULL,
	[fecha_fin] [date] NOT NULL,
	[activo] [bit] NOT NULL,
	[id_acreedor] [int] NOT NULL,
 CONSTRAINT [PK_cargos] PRIMARY KEY CLUSTERED 
(
	[id_cargo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
