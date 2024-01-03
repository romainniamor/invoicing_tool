<template>
  <div class="flex justify-end my-62">
    <div
      class="flex flex-col gap-6 mr-44 mt-24 mb-24 text-lg leading-loose"
      style="width: 880px"
    >
      <h2>Les mentions obligatoires à faire figurer sur une facture</h2>

      <ul class="text-justify list-disc">
        <li>votre nom si vous ne possédez pas de nom commercial</li>
        <li>
          votre dénomination sociale si vous avez créé une société (dans ce cas,
          doivent apparaitre le type de société et le montant de votre capital
          social
        </li>
        <li>
          Le n° RCS (Registre du Commerce et des Sociétés) suivi du nom de la
          ville où se trouve le greffe où est immatriculée l’entreprise, ou le
          n° de Répertoire des Métiers, la forme juridique
        </li>
        <li>L'adresse de facturation</li>
        <li>Le numéro du bon de commande</li>
        <li>Le capital social de l’assujetti et du client facturé</li>
        <li>
          Le n° d'identification de TVA de l'assujetti. Ce numéro doit figurer
          sur la facture, que l’opération soit réalisée en France, à destination
          d’un autre état membre, ou à l’exportation (pour les entreprises
          françaises : FR + 2 chiffres + n° de SIREN de l’entreprise)
        </li>
        <li>
          Le n° d'identification de TVA du client (facultatif pour les
          opérations effectuées en France). En cas d’échange intracommunautaire,
          le n° d’identification du client doit être indiqué, complété de la
          mention "Exonération de TVA, art. 262 ter-1 du code général des
          impôts"
        </li>
        <li>
          La date de délivrance de la facture (dès que la vente est réalisée, ou
          la prestation exécutée, le client doit être facturé)
        </li>
        <li>
          Le n° de la facture. La numérotation des factures est unique et
          continue, à partir d'une ou plusieurs séries (en fonction des
          catégories de clients)
        </li>
        <li>
          La dénomination précise (nature des articles et caractéristiques
          servant à identifier le produit)
        </li>
        <li>
          Le prix unitaire et la quantité (en unités, poids, ou en volume) des
          biens livrés ou de la prestation
        </li>
        <li>
          La date de livraison des biens ou de l'achèvement de la prestation de
          service
        </li>
        <li>Les éventuels rabais, remises, escomptes</li>
        <li>Les taux de TVA applicables et le montant de la TVA à payer</li>
        <li>Le prix unitaire hors TVA de chaque produit</li>
        <li>Le taux de TVA par produit</li>
        <li>
          Le total Hors Taxe des produits soumis au même taux de TVA si
          différents taux sont applicables
        </li>
        <li>Le montant total du prix HT, de la TVA et du prix TTC</li>
      </ul>
      <h2>Les mentions relatives</h2>
      <p>
        Les mentions relatives ne concernent pas les entreprises exonérées de
        TVA. Dans ce cas, il faut préciser sur les factures: "Exonération de
        TVA, art.262 ter-1 du CGI" - "TVA non applicable, art 293 B du CGI".
      </p>
      <p>
        Pour les entreprises autorisées à acquitter la TVA d’après les débits
        (prestataires de services), la mention "TVA payée sur les débits" doit
        être portée sur les factures.
      </p>
      <p>
        Les conditions d’escompte pour un paiement anticipé : si l’entreprise
        n’accorde pas d’escompte, elle doit le faire figurer sur sa facture.
      </p>
      <p>
        L'article L441-3 du Code de commerce ajoute l'obligation de fournir la
        date à laquelle le règlement doit intervenir (jour, mois et année).
      </p>
      <p>
        Il est conseillé d'y ajouter les conditions de règlement ainsi que le
        taux des pénalités de retard, surtout si vous n'avez pas annexé de
        conditions de vente ou de contrat à votre facture.
      </p>

      <h4>Les délais de paiement d'une facture</h4>
      <p>
        Le délai est de 30 jours suivant la réception du produit ou de la
        prestation, sauf dispositions contraires mentionnées dans les conditions
        générales de vente (voir art. L. 441-6 du Code de commerce). Le
        règlement est réputé réalisé à la date à laquelle les fonds sont mis par
        le client à la disposition du bénéficiaire ou de son subrogé.
      </p>
      <h4>Pénalités de retard</h4>
      <p>
        Le taux de ces pénalités peut être déterminé contractuellement, sinon
        c'est le taux de la Banque Centrale européenne, majoré de 7 points, qui
        s'applique. Le taux ne peut en aucun cas être inférieur à 1,5 fois le
        taux légal. Les pénalités de retard sont exigibles sans rappel préalable
        (voir art. L. 441-6 du Code de commerce).
      </p>
      <h4>Adhésion à un centre ou une association de gestion agréés</h4>
      <p>
        Pour bénéficier de l'abattement fiscal lié à cette adhésion, il faut
        indiquer que vous acceptez le paiement par chèque en ajoutant la mention
        : " Acceptant le règlement des sommes dues par chèques libellés à son
        nom en sa qualité de membre d'un centre de gestion agréé par
        l'administration fiscale ". Notez bien que toute mention manquante ou
        inexacte peut faire l'objet d'une amende de 15 €, sous réserve que cette
        dernière n'excède pas le quart du montant de la facture litigieuse
        (article 1737 II du CGI).
      </p>
      <h4>Régime fiscal de la micro-entreprise (franchise en base de TVA)</h4>
      <p>
        Vous ne facturez pas la TVA. Vos factures doivent alors porter la
        mention "T.V.A. non applicable, article 293 B du CGI".
      </p>
      <p>
        Le décret n° 2003-632 du 9 juillet 2003 transpose cette directive dans
        le droit français. Le nouvel article 289 du CGI renvoie pour la fixation
        de la liste des mentions obligatoires à porter sur les factures au 1er
        juillet 2003 à un décret en Conseil d'État qui a été publié le 9 juillet
        2003.
      </p>
      <nuxtLink
        to="https://www.economie.gouv.fr/cedef/facture-mentions-obligatoires"
        target="_blank"
      >
        <div class="mt-36 mb-36">
          <h2>Pour aller plus loin, <br />impot.gouv</h2>
        </div>
      </nuxtLink>
    </div>
  </div>
</template>

<style scoped>
h2 {
  position: relative;
}

h2::before {
  content: "";
  width: 12px;
  height: 100%;
  background-color: rgb(74 222 128);
  position: absolute;
  left: -25px;
  top: 0;
}

h2 {
  font-size: 3em;
  line-height: 1.1em;
  font-weight: 700;
  margin: 40px 0;
}

h4 {
  font-size: 1.8em;
  line-height: 1.1em;
  font-weight: 600;
  margin: 25px 0;
}
</style>
